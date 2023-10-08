from eventos.models import Evento, Palestrante, Palestra
from django.db import transaction


def seed_data():
    # Crie eventos
    with transaction.atomic():
        evento1 = Evento.objects.create(
            nome_do_evento="Conferência de Tecnologia 2023",
            data_do_evento="2023-11-20",
            descricao_do_evento="Uma conferência de tecnologia com palestras e workshops emocionantes.",
            local_do_evento="Centro de Convenções da Cidade"
        )

        evento2 = Evento.objects.create(
            nome_do_evento="Seminário de Design de UX",
            data_do_evento="2023-12-05",
            descricao_do_evento="Um seminário sobre Design de Experiência do Usuário (UX) com especialistas do setor.",
            local_do_evento="Auditório da Universidade"
        )

        # Adicione mais 3 eventos
        evento3 = Evento.objects.create(
            nome_do_evento="Conferência de Negócios 2023",
            data_do_evento="2023-09-15",
            descricao_do_evento="Uma conferência de negócios com foco em empreendedorismo e inovação.",
            local_do_evento="Hotel de Luxo"
        )

        evento4 = Evento.objects.create(
            nome_do_evento="Workshop de Marketing Digital",
            data_do_evento="2023-10-30",
            descricao_do_evento="Um workshop prático sobre estratégias de marketing digital.",
            local_do_evento="Espaço de Co-working"
        )

        evento5 = Evento.objects.create(
            nome_do_evento="Conferência de Saúde 2023",
            data_do_evento="2023-11-28",
            descricao_do_evento="Uma conferência de saúde com foco em bem-estar e medicina.",
            local_do_evento="Hospital da Cidade"
        )

    # Crie palestrantes
    with transaction.atomic():
        palestrante1 = Palestrante.objects.create(
            nome_do_palestrante="Alice Silva",
            resumo_do_palestrante="Designer de UX com 10 anos de experiência na indústria."
        )

        palestrante2 = Palestrante.objects.create(
            nome_do_palestrante="Carlos Souza",
            resumo_do_palestrante="Engenheiro de software e palestrante internacional."
        )

        # Adicione mais 6 palestrantes
        palestrante3 = Palestrante.objects.create(
            nome_do_palestrante="Maria Santos",
            resumo_do_palestrante="Médica renomada na área de saúde pública."
        )

        palestrante4 = Palestrante.objects.create(
            nome_do_palestrante="João Oliveira",
            resumo_do_palestrante="Empreendedor de sucesso e autor de best-sellers."
        )

        palestrante5 = Palestrante.objects.create(
            nome_do_palestrante="Patricia Lima",
            resumo_do_palestrante="Especialista em marketing digital e estratégias online."
        )

        palestrante6 = Palestrante.objects.create(
            nome_do_palestrante="Rafael Fernandes",
            resumo_do_palestrante="Engenheiro de software especializado em inteligência artificial."
        )

    # Crie palestras associadas a eventos e palestrantes
    with transaction.atomic():
        # Crie mais 8 palestras associadas aleatoriamente a eventos e palestrantes
        palestra3 = Palestra.objects.create(
            titulo_da_palestra="Design Thinking na Prática",
            descricao_da_palestra="Aplicação de Design Thinking em projetos do mundo real.",
            palestrante=palestrante1,

        )

        palestra4 = Palestra.objects.create(
            titulo_da_palestra="Inovação e Tecnologia",
            descricao_da_palestra="As últimas tendências em inovação tecnológica.",
            palestrante=palestrante2,
        )

        palestra5 = Palestra.objects.create(
            titulo_da_palestra="Empreendedorismo Digital",
            descricao_da_palestra="Estratégias para empreender no mundo digital.",
            palestrante=palestrante4,
        )

        palestra6 = Palestra.objects.create(
            titulo_da_palestra="Saúde Mental e Bem-Estar",
            descricao_da_palestra="Importância da saúde mental no ambiente de trabalho.",
            palestrante=palestrante3,
        )

        palestra7 = Palestra.objects.create(
            titulo_da_palestra="Marketing de Conteúdo",
            descricao_da_palestra="Como criar uma estratégia de marketing de conteúdo eficaz.",
            palestrante=palestrante5,
        )

        palestra8 = Palestra.objects.create(
            titulo_da_palestra="Inteligência Artificial e o Futuro",
            descricao_da_palestra="Impacto da inteligência artificial em nossas vidas.",
            palestrante=palestrante6,
        )


if __name__ == "__main__":
    seed_data()
