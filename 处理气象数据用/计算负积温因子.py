import pandas as pd

# 读取CSV文件
file_path = 'E:\gis\毕业论文\梁\\0114--0\sel_china_remapcon_tas_day_BCC_ssp126_2022_3_5_cn05grid_downscaled_nothern_sel.csv'
data = pd.read_csv(file_path)

# 计算负积温
def calculate_negative_degree_days(tas):
    # 假设温度数据 tas 单位为摄氏度
    threshold_temperature = 0  # 阈值温度
    negative_degree_days = tas[tas < threshold_temperature].sum()
    return negative_degree_days

# 按照经度（lon）和纬度（lat）分组，并计算负积温
result = data.groupby(['lat', 'lon']).agg({'tas': calculate_negative_degree_days}).reset_index()

# 输出结果到CSV文件
result.to_csv('E:\gis\毕业论文\梁\\0114--0\sel_china_remapcon_tas_day_BCC_ssp126_2022_3_5_cn05grid_downscaled_nothern_sel_negative_degree_days.csv', index=False)