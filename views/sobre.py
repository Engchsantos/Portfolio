import streamlit as st

from forms.contact import contact_form


@st.experimental_dialog("Contato")
def show_contact_form():
    contact_form()
st.markdown(
        "<p style='text-align: justify; color:#0070C0; font-size:20px'><b>Conheça meu portfólio de projetos!</b></p>",  unsafe_allow_html=True
    )
st.markdown(
        "<p style='text-align: justify; color:#0070C0; font-size:20px'>Aqui falo das minhas experiências, habilidades e algumas técnicas que utilizo no meu dia-a-dia profissional. No menu ao lado, você pode conhecer os principais projetos que participei, agrupados por tipo de obra.</p>",  unsafe_allow_html=True
    )
st.write("\n")

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/imagem_teste1.jpg", width=230)

with col2:
    st.markdown(
        "<p style='text-align: center; color:#0070C0; font-size:36px'><b>Carlos H. Santos</b></p>",  unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; color:black; font-size:20px'><b>Engenheiro Civil, especialista em gestão de projetos de construções e reformas</b></p>",  unsafe_allow_html=True
    )
    st.markdown("📧 Email: engchsantos@gmail.com")
    st.markdown("[Perfil no Linkedin](https://www.linkedin.com/in/engchsantos/)")
    if st.button("✉️ Contato"):
        show_contact_form()


st.write("\n")
st.markdown(
        "<p style='text-align: left; color:black; font-size:20px'><b><i>Experiências & Habilidades</i></b></p>",  unsafe_allow_html=True
    )
col11, col12 = st.columns(2, gap="small", vertical_alignment="top")
with col11:
       st.write(
        """
        - Mais de 10 anos de experiência em construção de prédios, obras comerciais e reformas residênciais
        - Estruturas de concreto armado, alvenaria estrutural, impermeabilizações, instalações e acabamentos
        - Liderança de equipes multidisciplinares
        - Normas de qualidade (ISO 9001 - PBQP-H)
        """
    )

with col12:
       st.write(
        """
        - Planejamento e controle de obras:  MS Excel, MS Project, Lean Construction
        - Leitura e construção de projetos: BIM, AutoCAD, Revit, Navisworks
        - Análise de dados e apresentações: Power BI, Python, SQL
        - Idiomas: Português e Inglês
        """
    )
import streamlit as st

st.write("\n")
st.markdown(
        "<p style='text-align: center; color:#0070C0; font-size:36px'>O que ofereço:</p>",  unsafe_allow_html=True
    )
st.write("\n")

st.markdown(
        "<p style='text-align: justify; color:gray; font-size:24px'><b>Com minha experiência e habilidades em gestão de projetos, coordeno equipes para garantir a entrega de reformas e construções dentro do prazo, orçamento e com a qualidade esperada, utilizando boas práticas de gestão. Sou proativo na remoção de impedimentos, mobilização de equipes, gestão de compras e na resolução de conflitos, assegurando o fluxo das atividades. A seguir, descrevo como utilizo essas habilidades nas principais fases de cada projeto:</b></p>",  unsafe_allow_html=True
    )
st.write("\n")


st.markdown(
        "<p style='text-align: justify; color:#0070C0; font-size:24px'><b>Fase de início:</b></p>",  unsafe_allow_html=True
    )
st.write("\n")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/inicio.png", width=460)

with col2:
    st.markdown(
        "<p style='text-align: justify; color:gray; font-size:18px'>Realizo uma análise completa das necessidades do cliente, revisando projetos e memoriais descritivos, assegurando o alinhamento entre o escopo do projeto, as expectativas e a viabilidade técnica. Defino objetivos claros, entregas e critérios de sucesso, possibilitando o monitoramento e controle de indicadores.</p>",  unsafe_allow_html=True
    )
st.write("\n")
st.markdown(
        "<p style='text-align: justify; color:#0070C0; font-size:20px'><i>Principalmente em reformas residenciais, tenho diversos exemplos de como essa etapa foi importante, onde na validação do escopo com cliente detectei discrepâncias e pude corrigir a tempo, prevenindo atrasos e custos adicionais.</i></p>",  unsafe_allow_html=True
    )

st.write("\n")
st.write("\n")
st.markdown(
        "<p style='text-align: justify; color:#0070C0; font-size:24px'><b>Planejamento:</b></p>",  unsafe_allow_html=True
    )
st.write("\n")

col3, col4 = st.columns(2, gap="small", vertical_alignment="center")
with col3:
    st.image("./assets/timeline.png", width=460)

with col4:
    st.markdown(
        "<p style='text-align: justify; color:gray; font-size:18px'> Utilizo o MS Project para desenvolver cronogramas, considerando recursos e dependências entre tarefas. Integro dados de quantitativos de materiais e mão de obra para uma previsão de custos precisa. Acompanho o progresso através de dashboards, permitindo uma melhor análise, para garantir o cumprimento do planejamento.</p>",  unsafe_allow_html=True
    )

st.markdown(
        "<p style='text-align: justify; color:#0070C0; font-size:20px'><i>Através desse processo de planejamento, consigo identificar as atividades críticas e direcionar os esforços para essas atividades. Com isso, já consegui evitar maiores atrasos em obras que já estavam em andamento, recuperando a confiança dos clientes.</i></p>",  unsafe_allow_html=True
    )

st.write("\n")

st.markdown(
        "<p style='text-align: justify; color:#0070C0; font-size:24px'><b>Fase de execução:</b></p>",  unsafe_allow_html=True
    )
st.write("\n")

col5, col6 = st.columns(2, gap="small", vertical_alignment="center")
with col5:
    st.image("./assets/execucao.png", width=460)

with col6:
    st.markdown(
        "<p style='text-align: justify; color:gray; font-size:18px'>Coordeno as equipes, garantindo a comunicação eficiente entre todos os envolvidos, desde times de suprimentos, equipes de produção e fornecedores. Monitoro o andamento do projeto, solucionando problemas e conflitos de forma proativa, sempre visando a eficiência e a segurança.</p>",  unsafe_allow_html=True
    )

st.markdown(
        "<p style='text-align: justify; color:#0070C0; font-size:20px'>Ao detectar um potencial atraso na conclusão das atividades, utilizei minha rede de contatos e minha habilidade de negociação para encontrar fornecedores e reforçar a equipe, garantindo a continuidade das obras sem impacto significativo no cronograma.</p>",  unsafe_allow_html=True
    )

st.write("\n")

st.markdown(
        "<p style='text-align: justify; color:#0070C0; font-size:24px'><b>Monitoramento e Controle:</b></p>",  unsafe_allow_html=True
    )
st.write("\n")

col7, col8 = st.columns(2, gap="small", vertical_alignment="center")
with col7:
    st.image("./assets/controle.png", width=460)

with col8:
    st.markdown(
        "<p style='text-align: justify; color:gray; font-size:18px'>Monitoro constantemente o progresso, comparando o desempenho real com o planejado. Utilizo a análise de dados e dashboards personalizados para identificar desvios e implementar ações corretivas. Através de relatórios, comunico regularmente o progresso aos stakeholders.</p>",  unsafe_allow_html=True
    )

st.markdown(
        "<p style='text-align: justify; color:#0070C0; font-size:20px'>Através do acompanhamento detalhado dos custos e do progresso físico das obras, via dashboards e análise de dados, identifiquei um desvio no orçamento e, com base em informações precisas, propus medidas corretivas, evitando um aumento significativo dos custos finais.</p>",  unsafe_allow_html=True
    )

st.write("\n")

st.markdown(
        "<p style='text-align: justify; color:#0070C0; font-size:24px'><b>Encerramento:</b></p>",  unsafe_allow_html=True
    )


col9, col10 = st.columns(2, gap="small", vertical_alignment="center")
with col9:
    st.image("./assets/encerramento.png", width=460)

with col10:
    st.markdown(
        "<p style='text-align: justify; color:gray; font-size:18px'>Conduzo o processo de encerramento formal, fornecendo o as-built, gerando de relatórios sobre a obra e o arquivamento de documentos. Isso garante o aprendizado e a melhoria contínua para projetos futuros.</p>",  unsafe_allow_html=True
    )
