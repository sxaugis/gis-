library(terra)
library(dplyr)
library(ggplot2)
library(reservoir)

folder  <- "D:\\gis\\毕业论文\\林\\FVC";
folder<- list.files(folder,pattern = '\\.tif$',full.names = TRUE)
path <- folder[order(as.numeric(gsub("\\D","",folder)))]

firs <- rast(path)


firs_sen = app(firs,Hurst,cores=28)


plot(firs_sen)
writeRaster(firs_sen,filename = "D:\\gis\\毕业论文\\林\\FVC\\hurst.tif")