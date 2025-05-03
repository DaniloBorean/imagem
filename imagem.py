from PIL import Image, ImageFilter

def abrir_imagem(caminho):
    """Abre uma imagem do caminho especificado."""
    return Image.open(caminho)

def salvar_imagem(imagem, caminho):
    """Salva a imagem no caminho especificado."""
    imagem.save(caminho)

def redimensionar(imagem, nova_largura, nova_altura):
    """Redimensiona a imagem para as novas dimensões."""
    return imagem.resize((nova_largura, nova_altura))

def converter_para_cinza(imagem):
    """Converte a imagem para escala de cinza."""
    return imagem.convert('L')

def aplicar_filtro_borrado(imagem):
    """Aplica um filtro de desfoque na imagem."""
    return imagem.filter(ImageFilter.BLUR)

def aplicar_filtro_contorno(imagem):
    """Aplica um filtro de contorno na imagem."""
    return imagem.filter(ImageFilter.CONTOUR)