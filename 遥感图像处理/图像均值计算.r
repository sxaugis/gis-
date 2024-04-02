library(terra)
library(dplyr)
library(ggplot2)
library(gtools)

folder  <- "D:\\gis\\毕业论文\\林\\FVC";
folder<- list.files(folder,pattern = '\\.tif$',full.names = TRUE)
path <- folder[order(as.numeric(gsub("\\D","",folder)))]

fvc_data<- data.frame(year = numeric(),fvc= numeric())
fvc_data[1:24,"year"]<- 2000:2023
for (i in 1:length(path))
{
  img<- rast(path[i])
  mean_fvc<- mean(values(img),na.rm=TRUE)
  fvc_data[i,'fvc']<- mean_fvc
}
lm_model <- lm(fvc ~ year, data = fvc_data)

# 打印回归结果
print(summary(lm_model))

# 绘制散点图和回归线
p <- ggplot(fvc_data, aes(x = year, y = fvc)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE) +
  ggtitle("Annual Mean FVC Regression") +
  labs(x = "Year", y = "Mean FVC") +
  theme_minimal()