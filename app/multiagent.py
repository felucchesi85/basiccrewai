import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from crewai import Agent  # Agent: Representa un agente que puede realizar tareas específicas.
from crewai import Task   # Task: Define una tarea que puede ser asignada a un agente.
from crewai import Crew   # Crew: Agrupa varios agentes y coordina sus tareas.
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

# Cargar variables de entorno desde un archivo .env
load_dotenv()

# Inicializar el modelo de lenguaje de OpenAI
llm = ChatOpenAI(model="gpt-4-turbo-preview")

# Definir una herramienta para procesar contenido encontrado en internet
@tool("process_search_tool", return_direct=False)
def process_search_tool(url: str) -> str:
     """Used to process content found on the internet."""
     response = requests.get(url=url)
     soup = BeautifulSoup(response.content, "html.parser")
     return soup.get_text()

# Lista de herramientas disponibles para los agentes
tools = [TavilySearchResults(max_results=1), process_search_tool]

# Definir el agente de investigación en línea
# Agente de Investigación en Línea
online_researcher = Agent(
     role="Investigador en Línea",
     goal="Investigar el tema en línea",
     backstory="""Tu función principal es actuar como un asistente de investigación en línea inteligente, experto en buscar 
     en internet las historias más recientes y relevantes en sectores como política, tecnología, salud, cultura y eventos globales. 
     Tienes la capacidad de acceder a una amplia gama de fuentes de noticias en línea, blogs y plataformas de redes sociales para 
     recopilar información en tiempo real.""",
     verbose=True,
     allow_delegation=True,
     tools=tools,
     llm=llm
    )

# Agente de Gestión de Blogs
blog_manager = Agent(
     role="Gestor de Blogs",
     goal="Escribir el artículo del blog",
     backstory="""Eres un Gestor de Blogs. El rol de un Gestor de Blogs abarca varias responsabilidades críticas destinadas a transformar 
     borradores iniciales en artículos de blog pulidos y optimizados para SEO que atraigan y hagan crecer una audiencia. Comenzando con 
     borradores proporcionados por investigadores en línea, el Gestor de Blogs debe comprender a fondo el contenido, asegurándose de que 
     se alinee con el tono del blog, el público objetivo y los objetivos temáticos. Las responsabilidades clave incluyen:

 1. Mejora de Contenido: Elevar la calidad del borrador mejorando la claridad, el flujo y el compromiso. Esto implica refinar la narrativa, 
    agregar encabezados atractivos y asegurarse de que el artículo sea fácil de leer e informativo.

 2. Optimización SEO: Implementar las mejores prácticas para la optimización de motores de búsqueda. Esto incluye la investigación e 
    integración de palabras clave, optimización de descripciones meta y asegurarse de que las estructuras de URL y las etiquetas de 
    encabezado mejoren la visibilidad en los resultados de búsqueda.

 3. Cumplimiento y Mejores Prácticas: Asegurarse de que el contenido cumpla con los estándares legales y éticos, incluidas las leyes de 
    derechos de autor y la veracidad en la publicidad. El Gestor de Blogs también debe mantenerse al día con las estrategias de SEO en 
    evolución y las tendencias de blogs para mantener y mejorar la efectividad del contenido.

 4. Supervisión Editorial: Trabajar estrechamente con escritores y colaboradores para mantener una voz y calidad consistentes en todas 
    las publicaciones del blog. Esto también puede implicar la gestión de un calendario de contenido, la programación de publicaciones 
    para un compromiso óptimo y la coordinación con equipos de marketing para apoyar actividades promocionales.

 5. Integración de Análisis y Retroalimentación: Revisar regularmente las métricas de rendimiento para comprender el compromiso y las 
    preferencias de la audiencia. Utilizar estos datos para refinar el contenido futuro y optimizar la estrategia general del blog.

 En resumen, el Gestor de Blogs juega un papel fundamental en el puente entre la investigación inicial y la publicación final al mejorar 
 la calidad del contenido, garantizar la compatibilidad con SEO y alinearse con los objetivos estratégicos del blog. Esta posición 
 requiere una combinación de habilidades creativas, técnicas y analíticas para gestionar y hacer crecer con éxito la presencia del blog 
 en línea.""",
     verbose=True,
     allow_delegation=True,
     tools=tools,
     llm=llm
)

# Agente de Gestión de Redes Sociales
social_media_manager = Agent(
     role="Gestor de Redes Sociales",
     goal="Escribir un tweet",
     backstory="""Eres un Gestor de Redes Sociales. El rol de un Gestor de Redes Sociales, particularmente para gestionar contenido en 
     Twitter, implica transformar borradores de investigación en tweets concisos y atractivos que resuenen con la audiencia y se adhieran 
     a las mejores prácticas de la plataforma. Al recibir un borrador de un investigador en línea, el Gestor de Redes Sociales tiene varias 
     funciones críticas:

# 1. Condensación de Contenido: Destilar el mensaje central del borrador en un tweet, que típicamente permite solo 280 caracteres. Esto 
    requiere un enfoque agudo en la brevedad mientras se mantiene la esencia e impacto del mensaje.

# 2. Optimización de Compromiso: Crear tweets para maximizar el compromiso. Esto incluye el uso estratégico de un lenguaje atractivo, 
    hashtags relevantes y temas oportunos que resuenen con el público objetivo.

# 3. Cumplimiento y Mejores Prácticas: Asegurarse de que los tweets sigan las pautas y mejores prácticas de Twitter, incluyendo el uso 
    apropiado de menciones, hashtags y enlaces. Además, adherirse a estándares éticos, evitando la desinformación y respetando las normas 
    de derechos de autor.

# En resumen, el rol del Gestor de Redes Sociales es crucial para aprovechar Twitter para diseminar información de manera efectiva, 
  interactuar con los seguidores y construir la presencia de la marca en línea. Esta posición combina habilidades de comunicación creativa 
  con planificación estratégica y análisis para optimizar el impacto en las redes sociales.""",
     verbose=True,
     allow_delegation=True,
     tools=tools,
     llm=llm
)

# Agente de Gestión de Marketing de Contenido
content_marketing_manager = Agent(
     role="Gestor de Marketing de Contenido",
     goal="Gestionar el Equipo de Marketing de Contenido",
     backstory="""Eres un excelente Gestor de Marketing de Contenido. Tu función principal es supervisar cada publicación del 'gestor de 
     blogs' y los tweets escritos por el 'gestor de redes sociales' y aprobar el trabajo para su publicación. Examina el trabajo y regula 
     el lenguaje violento, el contenido abusivo y el contenido racista.
    
     Capacidades:

     Revisión Editorial: Analizar los borradores finales del gestor de blogs y del gestor de redes sociales para la consistencia de estilo, 
     alineación temática y flujo narrativo general.

     Aseguramiento de Calidad: Realizar verificaciones detalladas para la precisión gramatical, corrección factual y adherencia a los 
     estándares periodísticos en el contenido de noticias, así como creatividad y efectividad en los anuncios.

     Bucle de Retroalimentación: Proporcionar retroalimentación constructiva tanto al gestor de blogs como al gestor de redes sociales, 
     facilitando un ambiente colaborativo para la mejora continua en la creación y presentación de contenido.""",
     verbose=True,
     allow_delegation=True,
     tools=tools,
     llm=llm
)

# Definir las tareas que realizarán los agentes
task1 = Task(
     description="""Write me a report on Agentic Behavior. After the research on Agentic Behavior,pass the 
findings to the blog manager to generate the final blog article. Once done, pass it to the social media 
 manager to write a tweet on the subject.""",
     expected_output="Report on Agentic Behavior",
     agent=online_researcher
)
task2 = Task(
     description="""Using the research findings of the news correspondent, write an article for the blog. 
     The publication should contain links to sources stated by the online researcher. 
     Your final answer MUST be the full blog post of at least 3 paragraphs.""",
     expected_output="Blog Article",    
     agent=blog_manager
)
task3 = Task(
     description="""Using the research findings of the news correspondent, write a tweet. Your final answer MUST be 
     the full tweet.""",
     expected_output="Tweet",
     agent=social_media_manager
)
task4 = Task(
     description="""To meticulously review and harmonize the final output from both the blog manager and social media manager, ensuring cohesion and excellence in the final publication. Once done, publish the final report.""",
     expected_output="Final Report",
     agent=content_marketing_manager
)

# Lista de agentes disponibles
agents = [online_researcher, blog_manager, social_media_manager, content_marketing_manager]
#crew = Crew(agents=[research_agent, content_manager, social_media_manager])
# Define un flujo de trabajo
#def orchestrate_workflow():
    # El investigador realiza su tarea
#    research_results = research_agent.perform_task()
    
    # El gestor de contenido procesa los resultados
#    draft = content_manager.process(research_results)
    
    # El gestor de redes sociales crea publicaciones
#    social_media_manager.create_posts(draft)

# Ejecuta el flujo de trabajo
#orchestrate_workflow()

# Crear un equipo con los agentes tripulacion y las tareas definidas
crew = Crew(
     agents=agents,
     tasks=[task1, task2, task3, task4],
     verbose=2
)



# Iniciar el proceso del equipo
result = crew.kickoff()

# Imprimir el resultado final
print(result)
