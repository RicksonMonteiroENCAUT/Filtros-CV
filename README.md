# Filtros-CV
Aplicação em streamlit para análise de filtros e como alteram uma imagem

<h1>Comparação de Filtros</h1>

<p>Esta aplicação foi o primeiro projeto apresentado de forma mais simples na MasterClass de Visão Computacional disponibilizada pelo Carlos Melos.
No desenvolvimento do projeto acrescentei algumas controles por slide. O tamanho do Kernel do <a href="https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html#gaussian-filtering" target="_blank">filtro gaussiano</a>. Dessa forma, foi possivel analisar como as suas dimensão influênciam na suavização causada na imagem, quanto maior o tamanho do kernel,  maior o desfoque
podemos ver a comparação abaixo:</p>
<div class=01> 
    <img src="https://user-images.githubusercontent.com/62216467/103288036-c1de8180-49c2-11eb-8e1d-408570b333d6.jpeg" width=300 alt="Original">  
    <img src="https://user-images.githubusercontent.com/62216467/103287987-a2475900-49c2-11eb-8398-3298f28d5398.jpeg" width=300 alt="Kernel (9x9)"> 
    <img src="https://user-images.githubusercontent.com/62216467/103287990-a4a9b300-49c2-11eb-89be-2dfcafba8fb6.jpeg" width=300 alt="Kernel (15x15)">
</div>
</br>
<p>Acima temos, respectivamente a imagem original, após aplicação do filtro gaussiano com kernel (9x9) e com Kernel (15x15).
Vale Ressaltar que foi utilizado o borderType=cv2.BORDER_DEFAULT, em algumas comparações que fiz, percebi que a escolha desse parâmetro gera uma menor conservação de bordas em comparação com cv2.BORDER_CONSTANT, mas melhor que os cv2.BORDER_TRANSPARENT e cv2.BORDER_ISOLATED. 
O critério que utilizei foi uma maior facilidade em distinguir as trocas de  cores em diferentes pontos da imagem. "Onde ainda seria parte da blusa ou parte do fundo após um desfoque alto".
</p>
<h2>Detector de Bordas</h2>
<p>De mesmo modo, criei uma aplicação semelhante para analisar o  comportamento do algoritimo Canny para detecção de bordas e como ele se comporta com a variação dos tresholds impostos, bem como com a variação do kernel usado no filtro gaussiano aplicado antes do algoritmo para redução de ruídos. 
Você pode entender um pouco mais sobre o funcionamento do método neste <a href="https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html" target="_blank">link</a>. Abaixo temos a imagem após a aplicação do algoritmo</p>
<div class=01> 
    <img src="https://user-images.githubusercontent.com/62216467/103288036-c1de8180-49c2-11eb-8e1d-408570b333d6.jpeg" width=400 alt="Original">  
    <img src="https://user-images.githubusercontent.com/62216467/103291776-446b3f00-49cb-11eb-8046-dcba717d2397.jpeg" width=400 alt="Canny"> 
</div>
<p>
   Na imagem acima foram aplicados um kernel (15x15) no filtro gaussiano e borderType=cv2.BORDER_CONSTANT, afim de manter uma maior quantidade de bordas. No tresholding inferior um valor de igual à 30 e o superior igual à 40.
</p>
<h2>Conclusão</h2>
<p>
  O projeto proposto foi bastante interessante, pude compreender mais sobre o funcionamento de certos filtros, bem como suas utilidades no âmbito da visão computacional. Essa aplicação possui outros filtros como o grayScale, sépia, sketch, controle de contraste, saturação, entre outros. Compilem o código localmente na maquina de vocês (streamlit run main.py) e me digam o que acharam para podermos progredir juntos hahah!
  Grande Abraço!!
  Qualquer algo a ser acrescentado, alguma dúvida, bem como críticas serão totalmente bem vindas!;) 
</p>
<h2>Aplicação</h2>
<div class=01> 
    <img src="https://user-images.githubusercontent.com/62216467/103294219-29e79480-49d0-11eb-9672-277e47b04cf9.jpeg" width=400 alt="Original">  
</div>
<p>
    <a href="https://www.instagram.com/rickson_gm/" target="_blank">Instagram</a>
    <a href="https://www.gmail.com" target="_blank">ricksonencaut@gmail.com</a>
    <a href="https://www.linkedin.com/in/rickson-gomes-monteiro-411a2a1a1/" target="_blank">LinkedIN</a>
</p>




