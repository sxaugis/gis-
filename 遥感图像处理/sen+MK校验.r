library(terra)
library(dplyr)
library(ggplot2)
library(trend)

folder  <- "D:\\gis\\毕业论文\\林\\FVC";
folder<- list.files(folder,pattern = '\\.tif$',full.names = TRUE)
path <- folder[order(as.numeric(gsub("\\D","",folder)))]

firs <- rast(path)

fun_sen <- function(x){
  if(length(na.omit(x)) <24) return(c(NA, NA, NA))  
  MK_estimate <- trend::sens.slope(ts(na.omit(x), start = 0, end = 23, frequency = 1), conf.level = 0.95) 
  slope <- MK_estimate$estimates
  MK_test <- MK_estimate$p.value
  Zs <- MK_estimate$statistic
  return(c(Zs, slope, MK_test))
}

firs_sen = app(firs,fun_sen,cores=28)
names(firs_sen) = c("Z","slope","p-value")

plot(firs_sen)
writeRaster(firs_sen,filename = "D:\\gis\\毕业论文\\林\\FVC\\slope.tif",names = firs_sen@cpp[["names"]])