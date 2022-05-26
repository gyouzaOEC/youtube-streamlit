
import streamlit as st



st.title("お試し版だよ")

st.write("progress bar")
"start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f"Iteration {i+1}")
  bar.progress(i+1)
  time.sleep(0.05)


"Done!!!!!!"











# left_column , right_column = st.beta_columns(2)
# button = left_column.button("words appear in right column")
# if button:
#   right_column.write("here is rigth column")

# expander = st.beta_expander("Q&A")
# expander.write("問い合わせ番号を書く")






text = st.text_input("Please tell me your hobby")

"Your hobby is ", text , "."


condtion = st.slider("how are you?", 0, 100, 50)

"your condition is ", condtion , "."






# if st.checkbox("Show Image"):
#   img = Image.open("080305_1803~01.JPG")
#   st.image(img, caption="三井寿", use_column_width=True)