import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit テスト")

# # st.write("プログレスバーの表示")
# """
# ## プログレスバーの表示
# """
# "Start!!"

# latest_iteration = st.empty()
# bar = st.progress(0)


# for i in range(100):
#     latest_iteration.text(f"{i+1} %")
#     bar.progress(i + 1)
#     time.sleep(0.01)
#     if i+1 == 100:
#         done = False

# "Done!!!"

# st.write("Mapping")
"""
## Mapping
--------
"""
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=["lat", "lon"]
)

# mapping
if st.checkbox("Show Maps"):
    st.map(df)

# DataFrameを表示
# st.dataframe(df.style.highlight_max(axis=0))

# 折れ線グラフを表示
# st.line_chart(df)

# 折れ線(領域を囲む)
# st.area_chart(df)

# 棒グラフ
# st.bar_chart(df)

#st.write("Display Image")
"""
## Display Image
--------
"""
if st.checkbox("Show Image"):
    img = Image.open("logo.png")
    st.image(img, caption="Streamlit Logo",
             use_column_width=True)


#st.write("Display Video")
"""
## Display Video
--------
"""
# Video
if st.checkbox("Show Video"):
    st.video("https://youtu.be/B2iAodr0fOo")

# """
# ## Markdown記法も使える
# ----
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# st.latex(r'''
#      a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#      \sum_{k=0}^{n-1} ar^k =
#      a \left(\frac{1-r^{n}}{1-r}\right)
#      ''')


"""
## Interactive Widgets
--------
"""
st.write("Interactive Widgets")

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander = st.expander("問い合わせ")
expander.text_input("問い合わせ1")


# option = st.selectbox(
#     "好きな数字を教えて下さい",
#     list(range(1, 11))
# )
# "あなたの好きな数字は、", option, "です。"

# text = st.sidebar.text_input("あなたの趣味を教えて下さい",)
# condition = st.sideber.slider("あなたの今の調子は?", 0, 100, 50)

# "あなたの趣味:", text
# if condition < 30:
#     "コンディションはあまり良くないみたいですね。"
# elif condition < 80:
#     "コンディションはまあまあですね。"
# else:
#     "コンディションはバッチリですね！"
