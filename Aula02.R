################################################################################################
#########################################   GRAFICOS    ########################################
################################################################################################

################################################################################################
# Plotar uma funcao quadratica de -10 a 10 (de 1 em 1)
################################################################################################
rm(list=ls())
x<-seq(-10,10,1)   # Sequencia de -10 a 10 passo 1
y<-x^2             # Funcao y = x^2
plot(x,y,type="l") # Plota grafico com linhas
################################################################################################
# Plotar uma funcao seno de 0 a 2pi e seus respectivos pontos (de 0.1 em 0.1)
################################################################################################
x<-seq(0,2*pi,0.1) # Gerando pontos
y<-sin(x)          # Funcao Seno
plot(x,y,type='l') # Plota grafico
par(new=TRUE)      # Juntar graficos
plot(x,y,type='p') # Inserir pontos no grafico
################################################################################################
# Gerar 2 sequencias de -25 a 25. Gerar uma matriz em que o numero de linhas e colunas sejam o 
# tamanho das sequencias. Plotar matriz 3D, 26 x 26, tal que o conteudo da matriz seja dado por:
# M[ci,cj]<-i^3 + j^3 + 6*i*j
################################################################################################
library('plot3D')   # Utilizar pacote
seqi<-seq(-25,25,2) # Gerar sequencia
seqj<-seq(-25,25,2) # Gerar sequencia
M<-matrix(1,nrow=length(seqi),ncol=length(seqj))  #Gerar matriz
ci<-0
for (i in seqi)
  {
     ci<-ci+1
     cj<-0
     for (j in seqj) 
       {
         cj<-cj+1
         M[ci,cj]<-i^3 + j^3 + 6*i*j # Funcao 
       }
  }
persp3D(seqi,seqj,M,contour=T) #Plotar em 3D
################################################################################################
# DISTRIBUICAO NORMAL
################################################################################################
xc1<-rnorm(30)*0.5+2     #Gerando uma DN normal em 2
xc2<-rnorm(30)*0.5+4     #Gerando uma DN normal em 4
plot(xc1,matrix(0,length(xc1)),col='red',xlim=c(0,6),ylim=c(0,1),xlab='',ylab='')  #Plot
par(new=T)
plot(xc2,matrix(0,length(xc2)),col='blue',xlim=c(0,6),ylim=c(0,1),xlab='',ylab='') #Plot
hist(xc1)
hist(xc2)
################################################################################################
# DISTRIBUICAO NORMAL DE DUAS VARIAVEIS
################################################################################################
s1<-0.5
s2<-0.5
nc<-100
xc1<-matrix(rnorm(nc*2),ncol=2)*s1 + matrix(c(2,2),nrow=nc,ncol=2) #Criando matriz
xc2<-matrix(rnorm(nc*2),ncol=2)*s2 + matrix(c(4,4),nrow=nc,ncol=2) #Criando matriz
plot(xc1[,1],xc1[,2],type="p",col='red',xlim=c(0,6),ylim=c(0,6),xlab='',ylab='')
par(new=T)
plot(xc2[,1],xc2[,2],type="p",col='blue',xlim=c(0,6),ylim=c(0,6))
################################################################################################################################################################################################
# ESTIMATIVAS
################################################################################################
m1<-mean(xc1)   #Media
s1<-sd(xc1)     #Desvio Padrao
var1<-var(xc1)  #Variancia
m2<-mean(xc2)
s2<-sd(xc2)
var2<-var(xc2)
