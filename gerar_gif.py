import os
from PIL import Image, ImageDraw, ImageFont


# ==============================================================================
# CONFIGURAÇÕES
# ==============================================================================

CONFIG = {

    # --------------------------------------------------------------------------
    # ARQUIVOS
    # --------------------------------------------------------------------------

    "nome_arquivo": "terminal_vintage.gif",
    "imagem_fundo": "perfil.png",

    # --------------------------------------------------------------------------
    # ORDEM DOS IDIOMAS
    # --------------------------------------------------------------------------

    "ordem_idiomas": ["EN", "ES", "PT"],

    # --------------------------------------------------------------------------
    # CURSOR
    # --------------------------------------------------------------------------

    "quantidade_piscadas": 3,

    "duracao_cursor_visivel": 200,
    "duracao_cursor_invisivel": 200,

    # --------------------------------------------------------------------------
    # DIGITAÇÃO
    # --------------------------------------------------------------------------

    "duracao_por_caractere": 60,

    # --------------------------------------------------------------------------
    # INTERVALOS
    # --------------------------------------------------------------------------

    "intervalo_entre_ciclos": 3000,
    "duracao_final": 5000,

    # --------------------------------------------------------------------------
    # LAYOUT
    # --------------------------------------------------------------------------

    "tamanho_fonte": 24,
    "espacamento_linha": 15,

    "x_inicial": 560,
    "y_inicial": 200,

    # --------------------------------------------------------------------------
    # PROMPT / CURSOR
    # --------------------------------------------------------------------------

    "prompt": "$ ",
    "cursor": "_",

    # --------------------------------------------------------------------------
    # IDIOMA
    # --------------------------------------------------------------------------

    "mostrar_indicador_idioma": True,

    "formato_indicador_idioma": "[{codigo}] {nome}",

    # --------------------------------------------------------------------------
    # CORES
    # --------------------------------------------------------------------------

    "cor_prompt": (201, 209, 217),
    "cor_rotulo": (242, 141, 53),
    "cor_valor": (141, 231, 241),
    "cor_idioma": (201, 209, 217),

    # --------------------------------------------------------------------------
    # GIF
    # --------------------------------------------------------------------------

    "loop": 0,
    "optimize": False,
    "dither": False,
}


# ==============================================================================
# IDIOMAS
# ==============================================================================

IDIOMAS = {

    "EN": {
        "nome": "English",

        "linhas": [
            " ",
            "Name: ............. Carlos Magno R. de Assis",
            "Role: ............. AI Engineer | LLMs & RAG | AI Security",
            "Location: ......... Brazil (Remote)",
            "Focus: ............ AI Engineering, Intelligent Systems & Data",
            "Stack: ............ Python, PostgreSQL, Docker, Ollama, MinIO, Power BI",
            "Specialties: ...... LLMs, RAG, AI Security, Prompt Engineering",
            "Experience: ....... Software Development, AI & Data Analytics",
            " ",
            "CONTACT",
            "Email: ............ cmrda@outlook.com",
            "GitHub: ........... Magno-Rodigues",
            "LinkedIn: ......... linkedin.com/in/cmrda",
        ],
    },


    "PT": {
        "nome": "Português",

        "linhas": [
            " ",
            "Nome: .............. Carlos Magno R. de Assis",
            "Atuação: ........... AI Engineer | LLMs & RAG | AI Security",
            "Localização: ....... Brasil (Remoto)",
            "Foco: .............. Engenharia de IA, Sistemas Inteligentes & Dados",
            "Stack: ............. Python, PostgreSQL, Docker, Ollama, MinIO, Power BI",
            "Especialidades: .... LLMs, RAG, AI Security, Prompt Engineering",
            "Experiência: ....... Software Development, AI & Data Analytics",
            " ",
            "CONTATO",
            "Email: ............. cmrda@outlook.com",
            "GitHub: ............ Magno-Rodigues",
            "LinkedIn: .......... linkedin.com/in/cmrda",
        ],
    },


    "ES": {
        "nome": "Español",

        "linhas": [
            " ",
            "Nombre: ............ Carlos Magno R. de Assis",
            "Rol: ............... AI Engineer | LLMs & RAG | AI Security",
            "Ubicación: ......... Brasil (Remoto)",
            "Enfoque: ........... Ingeniería de IA, Sistemas Inteligentes & Datos",
            "Stack: ............. Python, PostgreSQL, Docker, Ollama, MinIO, Power BI",
            "Especialidades:..... LLMs, RAG, AI Security, Prompt Engineering",
            "Experiencia: ....... Desarrollo de Software, IA & Data Analytics",
            " ",
            "CONTACTO",
            "Email: ............. cmrda@outlook.com",
            "GitHub: ............ Magno-Rodigues",
            "LinkedIn: .......... linkedin.com/in/cmrda",
        ],
    },
}


# ==============================================================================
# ATALHOS DE CONFIGURAÇÃO
# ==============================================================================

NOME_ARQUIVO = CONFIG["nome_arquivo"]
IMAGEM_FUNDO = CONFIG["imagem_fundo"]

ORDEM_IDIOMAS = CONFIG["ordem_idiomas"]

QUANTIDADE_PISCADAS = CONFIG["quantidade_piscadas"]

DURACAO_CURSOR_VISIVEL = CONFIG["duracao_cursor_visivel"]
DURACAO_CURSOR_INVISIVEL = CONFIG["duracao_cursor_invisivel"]

DURACAO_FRAME = CONFIG["duracao_por_caractere"]

INTERVALO_ENTRE_CICLOS = CONFIG["intervalo_entre_ciclos"]
DURACAO_FINAL = CONFIG["duracao_final"]

TAMANHO_FONTE = CONFIG["tamanho_fonte"]
ESPACAMENTO_LINHA = CONFIG["espacamento_linha"]

X_INICIAL = CONFIG["x_inicial"]
Y_INICIAL = CONFIG["y_inicial"]

PROMPT = CONFIG["prompt"]
CURSOR = CONFIG["cursor"]

MOSTRAR_INDICADOR_IDIOMA = CONFIG["mostrar_indicador_idioma"]
FORMATO_INDICADOR_IDIOMA = CONFIG["formato_indicador_idioma"]

COR_PROMPT = CONFIG["cor_prompt"]
COR_ROTULO = CONFIG["cor_rotulo"]
COR_VALOR = CONFIG["cor_valor"]
COR_IDIOMA = CONFIG["cor_idioma"]

GIF_LOOP = CONFIG["loop"]
GIF_OPTIMIZE = CONFIG["optimize"]
GIF_DITHER = (
    Image.Dither.NONE
    if not CONFIG["dither"]
    else Image.Dither.FLOYDSTEINBERG
)


# ==============================================================================
# CARREGAMENTO
# ==============================================================================

def carregar_fundo():

    try:
        return Image.open(IMAGEM_FUNDO).convert("RGB")

    except IOError:

        print(
            f"Erro: Certifique-se de que a imagem "
            f"'{IMAGEM_FUNDO}' está na mesma pasta."
        )

        raise SystemExit(1)


def carregar_fonte():

    caminhos_fontes = [
        "consola.ttf",
        "cour.ttf",

        "/System/Library/Fonts/Constants/Courier.dfont",

        "/System/Library/Fonts/FontsAvailableAtRegistration/"
        "CourierNew.ttf",

        "/usr/share/fonts/truetype/dejavu/"
        "DejaVuSansMono.ttf",

        "/usr/share/fonts/TTF/"
        "DejaVuSansMono.ttf",
    ]

    for caminho in caminhos_fontes:

        try:

            fonte = ImageFont.truetype(
                caminho,
                TAMANHO_FONTE,
            )

            print(
                f"Fonte carregada com sucesso: {caminho}"
            )

            return fonte

        except IOError:
            continue

    try:

        return ImageFont.truetype(
            "Courier",
            TAMANHO_FONTE,
        )

    except IOError:

        return ImageFont.load_default()


# ==============================================================================
# TEXTO
# ==============================================================================

def dividir_linha(texto):

    if ":" in texto:

        partes = texto.split(":", 1)

        return (
            partes[0] + ":",
            partes[1],
        )

    return texto, ""


# ==============================================================================
# RENDERIZAÇÃO DE LINHA
# ==============================================================================

def desenhar_linha_colorida(
    draw,
    x,
    y,
    texto_completo,
    comprimento_max_digito=None,
):

    # --------------------------------------------------------------------------
    # Prompt
    # --------------------------------------------------------------------------

    draw.text(
        (x, y),
        PROMPT,
        fill=COR_PROMPT,
        font=font,
    )

    x_atual = (
        x
        + draw.textlength(
            PROMPT,
            font=font,
        )
    )

    # --------------------------------------------------------------------------
    # Digitação progressiva
    # --------------------------------------------------------------------------

    if comprimento_max_digito is not None:

        texto_exibir = (
            texto_completo[
                :comprimento_max_digito
            ]
        )

    else:

        texto_exibir = texto_completo

    rotulo, valor = dividir_linha(
        texto_exibir
    )

    # --------------------------------------------------------------------------
    # Rótulo
    # --------------------------------------------------------------------------

    if rotulo:

        draw.text(
            (x_atual, y),
            rotulo,
            fill=COR_ROTULO,
            font=font,
        )

        x_atual += draw.textlength(
            rotulo,
            font=font,
        )

    # --------------------------------------------------------------------------
    # Valor
    # --------------------------------------------------------------------------

    if valor:

        draw.text(
            (x_atual, y),
            valor,
            fill=COR_VALOR,
            font=font,
        )

        x_atual += draw.textlength(
            valor,
            font=font,
        )

    return x_atual


# ==============================================================================
# INDICADOR DE IDIOMA
# ==============================================================================

def texto_indicador_idioma(idioma):

    return FORMATO_INDICADOR_IDIOMA.format(
        codigo=idioma,
        nome=IDIOMAS[idioma]["nome"],
    )


def desenhar_linha_idioma(
    draw,
    x,
    y,
    idioma,
    comprimento_max_digito=None,
):

    texto = texto_indicador_idioma(idioma)

    # --------------------------------------------------------------------------
    # Prompt
    # --------------------------------------------------------------------------

    draw.text(
        (x, y),
        PROMPT,
        fill=COR_PROMPT,
        font=font,
    )

    x_atual = (
        x
        + draw.textlength(
            PROMPT,
            font=font,
        )
    )

    # --------------------------------------------------------------------------
    # Texto progressivo
    # --------------------------------------------------------------------------

    if comprimento_max_digito is not None:

        texto_exibir = texto[
            :comprimento_max_digito
        ]

    else:

        texto_exibir = texto

    draw.text(
        (x_atual, y),
        texto_exibir,
        fill=COR_IDIOMA,
        font=font,
    )

    return (
        x_atual
        + draw.textlength(
            texto_exibir,
            font=font,
        )
    )


# ==============================================================================
# LINHAS ANTERIORES
# ==============================================================================

def desenhar_linhas_anteriores(
    draw,
    linhas_anteriores,
):

    y_pos = Y_INICIAL

    for linha in linhas_anteriores:

        # ----------------------------------------------------------------------
        # Linha de idioma
        # ----------------------------------------------------------------------

        if linha.startswith(
            "__IDIOMA__:"
        ):

            idioma = linha.split(
                ":",
                1,
            )[1]

            desenhar_linha_idioma(
                draw,
                X_INICIAL,
                y_pos,
                idioma,
            )

        # ----------------------------------------------------------------------
        # Linha normal
        # ----------------------------------------------------------------------

        else:

            desenhar_linha_colorida(
                draw,
                X_INICIAL,
                y_pos,
                linha,
            )

        y_pos += (
            TAMANHO_FONTE
            + ESPACAMENTO_LINHA
        )

    return y_pos


# ==============================================================================
# PISCADA
# ==============================================================================

def adicionar_piscadas(
    frames,
    duracoes,
    fundo,
    linhas_anteriores,
):

    for _ in range(
        QUANTIDADE_PISCADAS
    ):

        # ----------------------------------------------------------------------
        # Cursor visível
        # ----------------------------------------------------------------------

        frame = fundo.copy()

        draw = ImageDraw.Draw(frame)

        y_pos = desenhar_linhas_anteriores(
            draw,
            linhas_anteriores,
        )

        draw.text(
            (X_INICIAL, y_pos),
            PROMPT + CURSOR,
            fill=COR_PROMPT,
            font=font,
        )

        frames.append(frame)

        duracoes.append(
            DURACAO_CURSOR_VISIVEL
        )

        # ----------------------------------------------------------------------
        # Cursor invisível
        # ----------------------------------------------------------------------

        frame = fundo.copy()

        draw = ImageDraw.Draw(frame)

        y_pos = desenhar_linhas_anteriores(
            draw,
            linhas_anteriores,
        )

        draw.text(
            (X_INICIAL, y_pos),
            PROMPT.rstrip(),
            fill=COR_PROMPT,
            font=font,
        )

        frames.append(frame)

        duracoes.append(
            DURACAO_CURSOR_INVISIVEL
        )


# ==============================================================================
# DIGITAÇÃO DE LINHA
# ==============================================================================

def adicionar_digitacao(
    frames,
    duracoes,
    fundo,
    linhas_anteriores,
    linha_atual,
):

    for i in range(
        len(linha_atual) + 1
    ):

        frame = fundo.copy()

        draw = ImageDraw.Draw(frame)

        # ----------------------------------------------------------------------
        # Linhas anteriores
        # ----------------------------------------------------------------------

        y_pos = desenhar_linhas_anteriores(
            draw,
            linhas_anteriores,
        )

        # ----------------------------------------------------------------------
        # Linha sendo digitada
        # ----------------------------------------------------------------------

        x_cursor = desenhar_linha_colorida(
            draw,
            X_INICIAL,
            y_pos,
            linha_atual,
            comprimento_max_digito=i,
        )

        # ----------------------------------------------------------------------
        # Cursor
        # ----------------------------------------------------------------------

        if i < len(linha_atual):

            draw.text(
                (x_cursor, y_pos),
                CURSOR,
                fill=COR_PROMPT,
                font=font,
            )

        frames.append(frame)

        duracoes.append(
            DURACAO_FRAME
        )


# ==============================================================================
# DIGITAÇÃO DO IDIOMA
# ==============================================================================

def adicionar_digitacao_idioma(
    frames,
    duracoes,
    fundo,
    idioma,
    linhas_anteriores,
):

    texto = texto_indicador_idioma(
        idioma
    )

    for i in range(
        len(texto) + 1
    ):

        frame = fundo.copy()

        draw = ImageDraw.Draw(frame)

        y_pos = desenhar_linhas_anteriores(
            draw,
            linhas_anteriores,
        )

        x_cursor = desenhar_linha_idioma(
            draw,
            X_INICIAL,
            y_pos,
            idioma,
            comprimento_max_digito=i,
        )

        if i < len(texto):

            draw.text(
                (x_cursor, y_pos),
                CURSOR,
                fill=COR_PROMPT,
                font=font,
            )

        frames.append(frame)

        duracoes.append(
            DURACAO_FRAME
        )


# ==============================================================================
# CICLO DE IDIOMA
# ==============================================================================

def adicionar_ciclo_idioma(
    frames,
    duracoes,
    fundo,
    idioma,
):

    linhas_anteriores = []

    # ==========================================================================
    # INDICADOR DO IDIOMA
    # ==========================================================================

    if MOSTRAR_INDICADOR_IDIOMA:

        # ----------------------------------------------------------------------
        # Pisca
        # ----------------------------------------------------------------------

        adicionar_piscadas(
            frames,
            duracoes,
            fundo,
            linhas_anteriores,
        )

        # ----------------------------------------------------------------------
        # Digita
        # ----------------------------------------------------------------------

        adicionar_digitacao_idioma(
            frames,
            duracoes,
            fundo,
            idioma,
            linhas_anteriores,
        )

        # ----------------------------------------------------------------------
        # Mantém o idioma na tela
        # ----------------------------------------------------------------------

        linhas_anteriores.append(
            f"__IDIOMA__:{idioma}"
        )

    # ==========================================================================
    # LINHAS DO PERFIL
    # ==========================================================================

    for linha_atual in IDIOMAS[idioma]["linhas"]:

        # ----------------------------------------------------------------------
        # Pisca antes de cada linha
        # ----------------------------------------------------------------------

        adicionar_piscadas(
            frames,
            duracoes,
            fundo,
            linhas_anteriores,
        )

        # ----------------------------------------------------------------------
        # Digitação caractere por caractere
        # ----------------------------------------------------------------------

        adicionar_digitacao(
            frames,
            duracoes,
            fundo,
            linhas_anteriores,
            linha_atual,
        )

        # ----------------------------------------------------------------------
        # Linha concluída
        # ----------------------------------------------------------------------

        linhas_anteriores.append(
            linha_atual
        )


# ==============================================================================
# PALETA GLOBAL
# ==============================================================================

def criar_paleta_global(frames):

    referencia = frames[-1].convert(
        "RGB"
    )

    paleta_referencia = referencia.quantize(
        colors=256,
        method=Image.Quantize.MEDIANCUT,
    )

    paleta = list(
        paleta_referencia.getpalette()
    )

    # --------------------------------------------------------------------------
    # Cores fixas
    # --------------------------------------------------------------------------

    cores_fixadas = [
        COR_PROMPT,
        COR_ROTULO,
        COR_VALOR,
    ]

    for indice, cor in enumerate(
        cores_fixadas
    ):

        posicao = indice * 3

        paleta[posicao] = cor[0]
        paleta[posicao + 1] = cor[1]
        paleta[posicao + 2] = cor[2]

    imagem_paleta = Image.new(
        "P",
        (1, 1),
    )

    imagem_paleta.putpalette(
        paleta
    )

    return imagem_paleta


def converter_frames_para_paleta(
    frames,
    paleta,
):

    return [
        frame.convert("RGB").quantize(
            palette=paleta,
            dither=GIF_DITHER,
        )
        for frame in frames
    ]


# ==============================================================================
# INTERVALO
# ==============================================================================

def adicionar_intervalo(
    frames,
    duracoes,
    duracao,
):

    if not frames or duracao <= 0:
        return

    frames.append(
        frames[-1].copy()
    )

    duracoes.append(
        duracao
    )


# ==============================================================================
# VALIDAÇÃO
# ==============================================================================

def validar_configuracao():

    if not ORDEM_IDIOMAS:

        raise ValueError(
            "ORDEM_IDIOMAS não pode estar vazia."
        )

    for idioma in ORDEM_IDIOMAS:

        if idioma not in IDIOMAS:

            raise ValueError(
                f"Idioma '{idioma}' "
                f"não existe em IDIOMAS."
            )

        if not IDIOMAS[idioma]["linhas"]:

            raise ValueError(
                f"O idioma '{idioma}' "
                f"não possui linhas."
            )


# ==============================================================================
# MAIN
# ==============================================================================

def main():

    validar_configuracao()

    global font

    fundo_limpo = carregar_fundo()
    font = carregar_fonte()

    frames = []
    duracoes_frames = []

    # ==========================================================================
    # CICLOS DOS IDIOMAS
    # ==========================================================================

    for indice, idioma in enumerate(
        ORDEM_IDIOMAS
    ):

        print(
            f"Gerando ciclo "
            f"{indice + 1}/"
            f"{len(ORDEM_IDIOMAS)}: "
            f"{idioma} - "
            f"{IDIOMAS[idioma]['nome']}"
        )

        adicionar_ciclo_idioma(
            frames,
            duracoes_frames,
            fundo_limpo,
            idioma,
        )

        # ----------------------------------------------------------------------
        # Intervalo entre idiomas
        # ----------------------------------------------------------------------

        if indice < len(
            ORDEM_IDIOMAS
        ) - 1:

            adicionar_intervalo(
                frames,
                duracoes_frames,
                INTERVALO_ENTRE_CICLOS,
            )

    # ==========================================================================
    # PAUSA FINAL
    # ==========================================================================

    adicionar_intervalo(
        frames,
        duracoes_frames,
        DURACAO_FINAL,
    )

    # ==========================================================================
    # PALETA
    # ==========================================================================

    print(
        "Criando paleta global..."
    )

    paleta = criar_paleta_global(
        frames
    )

    frames_paleta = (
        converter_frames_para_paleta(
            frames,
            paleta,
        )
    )

    # ==========================================================================
    # SALVAMENTO
    # ==========================================================================

    frames_paleta[0].save(
        NOME_ARQUIVO,
        save_all=True,
        append_images=frames_paleta[1:],
        optimize=GIF_OPTIMIZE,
        duration=duracoes_frames,
        loop=GIF_LOOP,
    )

    print()
    print(
        "GIF bicolor gerado com sucesso!"
    )
    print(
        f"Arquivo: "
        f"{os.path.abspath(NOME_ARQUIVO)}"
    )
    print(
        f"Frames: {len(frames_paleta)}"
    )


# ==============================================================================
# EXECUÇÃO
# ==============================================================================

if __name__ == "__main__":
    main()