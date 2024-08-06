import streamlit as st
import glob
import os
import base64

st.title('GIF 공유 웹 애플리케이션')

# GIF 파일 목록 및 태그
gif_directory = 'data'
category_list = glob.glob(os.path.join(gif_directory, "*"))
category_list.sort()

gifs_with_tags = {}

for category in category_list:
    category = os.path.basename(category)
    gifs_with_tags[category] = [
        "output_0.gif", 
        "output_1.gif", 
        "output_2.gif", 
        "output_3.gif", 
    ]

# 태그 버튼 생성
selected_tag = st.sidebar.selectbox('태그를 선택하세요:', list(gifs_with_tags.keys()))

# 선택된 태그에 따른 GIF 필터링
if selected_tag:
    filtered_gifs = gifs_with_tags[selected_tag]
else:
    filtered_gifs = []

st.write(f"총 {len(filtered_gifs)}개의 결과가 검색되었습니다.")

# 각 GIF 파일의 경로를 확인하고 HTML로 표시 (2x2 배열로 배치)
num_columns = 2
rows = [filtered_gifs[i:i + num_columns] for i in range(0, len(filtered_gifs), num_columns)]

for row in rows:
    cols = st.columns(num_columns)
    for col, gif in zip(cols, row):
        gif_path = os.path.join(gif_directory, selected_tag, gif)
        if os.path.exists(gif_path):
            with open(gif_path, "rb") as gif_file:
                gif_data = gif_file.read()
                b64_encoded_gif = base64.b64encode(gif_data).decode('utf-8')
                col.markdown(
                    f'<img src="data:image/gif;base64,{b64_encoded_gif}" '
                    f'width="100%" alt="{gif}" style="display:block;margin:auto;" loop=infinite />',
                    unsafe_allow_html=True
                )
        else:
            col.write(f"Error: {gif_path} 파일을 찾을 수 없습니다.")

st.write("위 GIF들은 예시로서 사용되었습니다.")
