rm(list=ls())
library("corpcor")
#############################################################################################################
#APROXIMACAO DE FUNCAO
#############################################################################################################
N<-200                         #Gerando dados
x<-runif(n=N,min=-15,max=10)   
xgrid<-seq(-15,10,1)
yr<-(0.5*x^2+3*x+10)+10*rnorm(length(x))
ygrid<-(0.5*xgrid^2+3*xgrid+10)
plot(x,yr,type='p',col='red',xlim=c(-15,10),ylim=c(-10,120),xlab='x',ylab='y') #Plot dos pontos
par(new=T)
plot(xgrid,ygrid,type='l',col='blue',xlim=c(-15,10),ylim=c(-10,120),xlab='x',ylab='y') #Plot da aproxima????o
