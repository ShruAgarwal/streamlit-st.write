import streamlit as st
import numpy as np
import altair as alt
import pandas as pd


st.title('**st.write()**')
st.write('Magic method for displaying text, numbers, DataFrames, plots and much more! 🤯')


st.subheader('1. Markdown-formatted text ---')
st.write('Hello from *Streamlit!* :sunglasses:')

st.subheader('2. Numbers ---')
st.write(1234)


st.subheader('3. Dataframes ---')
df = pd.DataFrame({
     'second column': [1, 2, 3, 4],
     'third column': [10, 20, 30, 40]
     })
st.write(df)


st.subheader('4. Multiple arguments ---')
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')


st.subheader('5. Chart objects ---')
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)


st.subheader('6. st.markdown()')
st.markdown('Streamlit is **_really_ cool!**.')

st.subheader('7. st.caption()')
st.caption('This is a  caption string that explains something above.')

st.subheader('8. st.latex() : SymPy expression to display as LaTeX 🤓')
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')



st.subheader('9. st.code() : Embed any code block!')
code = '''<script>
// using console.log
console.log('Hello from JavaScript!');
</script>'''
st.code(code, language='javascript')