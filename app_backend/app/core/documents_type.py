from enum import Enum

class DocumentType(str, Enum):
    LICENCA_PESCA = "Licença de Pesca"
    TITULO_PROPRIEDADE = "Título de Propriedade"
    IMPOSTO_CIRCULACAO = "Imposto de Circulação"
    DECLARACAO_RENDIMENTOS = "Declaração de Rendimentos"
    CERTIFICADO_SEGURANCA = "Certificado de Segurança"
    APOLICE_SEGURO = "Apólice de Seguro"
    LICENCA_CUMUNITARIA = "Licença Comunitária"
    DIARIO_BORDO = "Diário de Bordo"
    DECLARACAO_VENDA = "Declaração de Venda"
    CONTRIBUICAO_SEGURANCA_SOCIAL = "Contribuição para a Segurança Social"
    DECLARACAO_IVA = "Declaração de IVA"
    OUTROS = "Outros"