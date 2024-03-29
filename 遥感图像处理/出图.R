library(ggplot2)

# 创建数据框
data <- data.frame(
  year = c(2018, 2019, 2020, 2021, 2022),
  current_assets = c(41.48, 39.34, 36.95, 39.27, 37.5)
)

# 绘制折线图
ggplot(data, aes(x=year, y=current_assets)) +
  geom_line() +
  geom_point() +
  geom_text(aes(label=current_assets), vjust=-1.5, size=4) +
  scale_y_continuous(limits=c(0, 50), expand=c(0, 0)) +
  xlab("年份") + ylab("流动资产(亿)") +
  ggtitle("万达集团2018-2022年流动资产") +
  theme(plot.title = element_text(hjust = 0.5, size=18, face="bold", color="#4d4d4d"),
        axis.title.x = element_text(size=14, color="#4d4d4d"),
        axis.title.y = element_text(size=14, color="#4d4d4d"),
        axis.text.x = element_text(size=12, color="#4d4d4d"),
        axis.text.y = element_text(size=12, color="#4d4d4d"),
        panel.background = element_blank(),
        panel.grid.major = element_line(colour = "#e6e6e6"),
        panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        plot.margin = unit(c(1, 1, 1, 3), "cm"))
