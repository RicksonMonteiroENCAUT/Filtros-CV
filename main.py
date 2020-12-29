#Importação de Bibliotecas
import cv2
import numpy as np
import streamlit as st
from PIL import Image, ImageEnhance

def main():
    st.title('Masterclass Visão Computacional')
    st.markdown('Instagram: [@rickson_gm](https://www.instagram.com/rickson_gm/)')
    st.sidebar.title('Menu lateral')

    #Opções Menu:
    options= ['Filtros','Sobre']
    op=st.sidebar.selectbox('Selecione uma opção',options)
    #Filtros
    filtros= ['Original','GaussianBlur','Sketch','GrayScale','Sépia','Canny','Color','Contrast','Brightness','Sharpness']
    select_filter=st.sidebar.radio('Selecione o filtro',filtros)
    if op=='Filtros':
        #imagem inicial
        image_file=st.file_uploader('Carrega sua foto',type=['jpg','png','jpeg'])
        if image_file is not None:
            image=Image.open(image_file)
            st.sidebar.text('Imagem original:')
            st.sidebar.image(image, width=285)

            if select_filter=='Original':
                st.image(image, width=720)

            elif select_filter == 'GrayScale':
                img_convert=np.array(image.convert('RGB'))
                img_gray=cv2.cvtColor(img_convert,cv2.COLOR_RGB2GRAY)
                st.image(img_gray,width=720)
            elif select_filter== 'Sketch':
                img_convert=np.array(image.convert('RGB'))
                gray= cv2.cvtColor(img_convert,cv2.COLOR_RGB2GRAY)
                negativo=cv2.bitwise_not(gray)
                blur=cv2.GaussianBlur(gray,(25,25), cv2.BORDER_CONSTANT)
                sketch=cv2.divide(gray,cv2.bitwise_not(blur),scale=256)
                st.image(sketch, width=720)

            elif select_filter=='Sépia':
                alpha=st.sidebar.slider('Intesidade do kernel:',0.1,1.0,step=0.1)
                img_convert=np.array(image.convert('RGB'))
                img=cv2.cvtColor(img_convert,cv2.COLOR_RGB2BGR)
                kernel= np.array([[0.272, 0.534, 0.131],
                                  [0.349, 0.686, 0.168],
                                  [0.393, 0.769, 0.189]])
                sepia=cv2.filter2D(img,-1,kernel*alpha)
                st.image(sepia, channels='BGR',width=720)

            elif select_filter =='GaussianBlur':
                size=st.sidebar.slider('Kernel (N x N):',3,81,step=2)
                img_converted=np.array(image.convert('RGB'))
                img=cv2.cvtColor(img_converted,cv2.COLOR_RGB2BGR)
                #Gaussian blur aplica o filtro uniformemente em todos os canais, não há necessidade de converter para BGR
                blur=cv2.GaussianBlur(img,(size,size),cv2.BORDER_DEFAULT)
                st.image(blur, channels='BGR',width=720)

            elif select_filter =='Color':
                factor= st.sidebar.slider('Fator de cor:',0.0,2.0)
                enhancer= ImageEnhance.Color(image)
                color=enhancer.enhance(factor)
                st.image(color, width=720)

            elif select_filter == 'Contrast':
                factor = st.sidebar.slider('Fator de cor:', 0.0, 2.0)
                enhancer= ImageEnhance.Contrast(image)
                contrast= enhancer.enhance(factor)
                st.image(contrast, width=720)

            elif select_filter == 'Brightness':
                factor = st.sidebar.slider('Fator de Brilho:', 0.0, 2.0)
                enhancer= ImageEnhance.Brightness(image)
                brightness= enhancer.enhance(factor)
                st.image(brightness, width=720)

            elif select_filter == 'Sharpness':
                factor = st.sidebar.slider('Fator de Nitidez:', 0.0, 5.0)
                enhancer=ImageEnhance.Sharpness(image)
                sharpness= enhancer.enhance(factor)
                st.image(sharpness, width=720)

            else:
                kernel=st.sidebar.slider('Kernel Gaussiano (n x n):',9,27,step=2)
                tresh1=st.sidebar.slider('Limiar inferior:',0,127,step=5)
                tresh2 = st.sidebar.slider('Limiar superior:', tresh1, 255, step=5)
                img_converted=np.array(image.convert('RGB'))
                img=cv2.cvtColor(img_converted, cv2.COLOR_RGB2BGR)
                blur=cv2.GaussianBlur(img,(kernel,kernel),cv2.BORDER_CONSTANT)
                edge=cv2.Canny(blur,tresh1,tresh2)
                st.image(edge, width=720)
    elif op == 'Sobre':
        st.title('Sobre:')
        st.image(Image.open('Eu.jpg'),width=500)
        st.write('Me chamo Rickson Gomes Monteiro e tenho 19 anos. Atualmente estou cursando engenharia de controle e automação no Centro Federal de '
                'Educação Tecnológica de Minas Gerais em Leopoldina-Mg, cidade na qual me mudei no ano de 2019 para realizar o curso. '
                'Sou natural da cidade de Caetité-BA, onde sempre morei até minha saída para seguir meus sonhos. Sou um grande entusiasta de todas das áreas de IA '
                'e estarei compartilhando meu progresso durante meus estudos. Dessa forma, podemos avançar juntos nessa tão belíssima área.'
                 'Podem entrar em contato pelo meu [instagram]((https://www.instagram.com/rickson_gm/)), [ricksonencaut@gmail.com](https://www.gmail.com) ou [linkedIn](https://www.linkedin.com/in/rickson-gomes-monteiro-411a2a1a1/)')
        st.markdown('*Nunca é tarde para começar!*')




if __name__ =='__main__':
    main()