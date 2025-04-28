
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

st.set_page_config(layout= 'wide', page_title= 'Super_Market EDA', page_icon= '📊')

st.image('Supermrkets-near-Dubai-Hills-Estate-14th-Dec-c.jpg')

st.markdown("""<h1 style="color:orange;text-align:center;"> Super_Market EDA (Exploratory Data Analysis) </h1>""",
             unsafe_allow_html= True)

df = pd.read_csv('cleaned_data.csv', index_col= 0)
st.dataframe(df.head(10))



page = st.sidebar.radio('Pages', ['info', 'Univariate Analysis', 'Bivariate Analysis', 'Multivariate Analysis', 'Some Analysis'])

if page == 'info' :

    st.header('some info to describe numrical data')
    st.dataframe(df.describe().round(2))
    st.header('some info to describe catgorical data')
    st.dataframe(df.describe(include= 'object').round(2))
    df_corr = df.corr(numeric_only= True)
    st.header('some info to describe relation between  numrical columns')
    corr_gig = px.imshow(df_corr, text_auto= True, height= 800, width= 1200)
    st.plotly_chart(corr_gig)
    st.header('some fig to describe relation between  numrical columns')
    matrix = df.select_dtypes(include= "number")
    matrix_fig = px.scatter_matrix(matrix)
    st.plotly_chart(matrix_fig)

elif page == 'Univariate Analysis':

    tab_1, tab_2 = st.tabs(['Numerical Univariate Analysis', 'Categorical Univariate Analysis'])

    col = st.selectbox('Select Column', df.columns)
    
    chart = st.selectbox('Select Chart', ['Pie', 'Histogram', 'Box'])

    if chart == 'Histogram':
        st.plotly_chart(px.histogram(data_frame= df, x= col, color= col, title= col))

    elif chart == 'Box':
        st.plotly_chart(px.box(data_frame= df, x= col, title= col))

    elif chart == 'Pie':
        st.plotly_chart(px.pie(data_frame= df, names= col, title= col, hole = 0.5))


elif page == 'Bivariate Analysis':

    col_1, col_2 = st.columns(2, vertical_alignment= 'center')

    groupby_col = col_1.selectbox('Select groupby Column', ['City', 'Branch', 'Customer type', 'Gender', 'Product line',
    'Date', 'Payment', 'gross income', 'Rating', 'month', 'day', 'day_period'])

    filterd_col = col_1.selectbox('by Column', ['gross income', 'City', 'Branch', 'Customer type', 'Gender', 'Product line',
    'Total','Payment', 'Rating', 'month', 'day', 'day_period', 'Tax 5%'])

    agg_options = {'Sum': np.sum,'Count': 'count', 'Mean': np.mean}

    agg_choice = col_1.selectbox('Select aggregation function', options=list(agg_options.keys()))

    agg_func = agg_options[agg_choice]

    filtered_data = df.groupby(groupby_col)[filterd_col].agg(agg_func).sort_values(ascending=False).reset_index()

    available_columns = filtered_data.columns.tolist()

    chart = col_1.selectbox('Select Chart', ['bar', 'scatter', 'line', 'Box', 'strip', 'vision'])
    
    x_axis = col_1.selectbox('Select Column x', available_columns, index=0)
    
    y_axis = col_1.selectbox('Select Column y', available_columns, index=1 if len(available_columns) > 1 else 0)


    if chart == 'scatter':
        col_2.plotly_chart(px.scatter(data_frame= filtered_data, x= x_axis, y = y_axis, title= f"the {y_axis} with each {x_axis}"))

    elif chart == 'Box':
        col_2.plotly_chart(px.box(data_frame= filtered_data, x= x_axis, y = y_axis, title= f"the {y_axis} with each {x_axis}"))

    elif chart == 'line':
        col_2.plotly_chart(px.line(data_frame= filtered_data, x= x_axis, y = y_axis, title= f"the {y_axis} with each {x_axis}"))

    elif chart == 'bar':
        col_2.plotly_chart(px.bar(data_frame= filtered_data, x= x_axis, y = y_axis, title= f"the {y_axis} with each {x_axis}", text_auto= True))

    elif chart == 'vilion':
        col_2.plotly_chart(px.vilion(data_frame= filtered_data, x= x_axis, y = y_axis, title= f"the {y_axis} with each {x_axis}"))
    
    elif chart == 'strip':
        col_2.plotly_chart(px.strip(data_frame= filtered_data, x= x_axis, y = y_axis, title= f"the {y_axis} with each {x_axis}"))
    


elif page == 'Multivariate Analysis' :

    groupby_col = st.multiselect('Select groupby Column', ['City', 'Branch', 'Customer type', 'Gender', 'Product line',
    'Date', 'Payment', 'gross income', 'Rating', 'month', 'day', 'day_period'])

    filterd_col = st.selectbox('by Column', ['gross income', 'City', 'Branch', 'Customer type', 'Gender', 'Product line',
    'Total','Payment', 'Rating', 'month', 'day', 'day_period', 'Tax 5%'])

    agg_options = {'Sum': np.sum,'Count': 'count', 'Mean': np.mean}

    agg_choice = st.selectbox('Select aggregation function', options=list(agg_options.keys()))

    agg_func = agg_options[agg_choice]

    filtered_data = df.groupby(groupby_col)[filterd_col].agg(agg_func).sort_values(ascending=False).reset_index()

    available_columns = filtered_data.columns.tolist()

    hue_col = st.selectbox('coclor_col', ['Branch', 'City', 'Customer type', 'Gender', 'Product line',
       'Unit price', 'Quantity', 'Tax 5%', 'Total', 'Date', 'Payment', 'cogs',
       'gross income', 'Rating', 'month', 'day', 'day_period'])

    chart = st.selectbox('Select Chart', ['bar', 'scatter', 'line', 'Box', 'strip', 'vision'])
    
    x_axis = st.selectbox('Select Column x', available_columns, index=0)
    
    y_axis = st.selectbox('Select Column y', available_columns, index=1 if len(available_columns) > 1 else 0)


    if chart == 'scatter':
        st.plotly_chart(px.scatter(data_frame= filtered_data, x= x_axis, y = y_axis, color = hue_col, title= f"the {y_axis} with each {x_axis}", height = 800, width = 1200))

    elif chart == 'Box':
        st.plotly_chart(px.box(data_frame= filtered_data, x= x_axis, y = y_axis, title= f"the {y_axis} with each {x_axis}", height = 800, width = 1200))

    elif chart == 'line':
        st.plotly_chart(px.line(data_frame= filtered_data, x= x_axis, y = y_axis, title= f"the {y_axis} with each {x_axis}", height = 800, width = 1200))

    elif chart == 'bar':
        st.plotly_chart(px.bar(data_frame= filtered_data, x= x_axis, y = y_axis, text_auto= True, barmode= 'group', title= f"the {y_axis} with each {x_axis}", height = 800, width = 1200))

    elif chart == 'viloin':
        st.plotly_chart(px.viloin(data_frame= filtered_data, x= x_axis, y = y_axis, title= f"the {y_axis} with each {x_axis}", height = 800, width = 1200))
    
    elif chart == 'strip':
        st.plotly_chart(px.strip(data_frame= filtered_data, x= x_axis, y = y_axis, title= f"the {y_axis} with each {x_axis}", height = 800, width = 1200))

elif page == 'Some Analysis' :

    st.header('the most popular Branch')
    total_sales = df.groupby('Branch')['Total'].sum().round(2).sort_values(ascending= False).reset_index()
    st.plotly_chart(px.histogram(data_frame= total_sales, x= 'Branch', y= 'Total', text_auto= True))

    popular_branch = df['Branch'].value_counts().reset_index()
    st.plotly_chart(px.pie(data_frame= popular_branch , names= 'Branch', values= 'count', hole= 0.5))

    st.header('the most city do best sales')
    highest_total_per_city = df.groupby(['City', 'Branch'])['Total'].sum().sort_values(ascending= False).reset_index()
    st.plotly_chart(px.histogram(data_frame= highest_total_per_city, x= 'City', y= 'Total', color = 'Branch' ,text_auto= True))

    st.header('The most consuming gender')
    total_sales_per_gender = df.groupby(['City', 'Gender'])['Total'].sum().sort_values(ascending= False).reset_index()
    st.plotly_chart(px.histogram(data_frame= total_sales_per_gender, x= 'City', y= 'Total', color = 'Gender' , text_auto= True, barmode= 'group'))

    st.header('The most product lines achives the top-selling')
    the_highest_prouduct_lines = df.groupby(['Product line'])['Total'].sum().sort_values(ascending= False).reset_index()
    st.plotly_chart(px.bar(data_frame= the_highest_prouduct_lines, x= 'Product line', y= 'Total', color= 'Product line', text_auto= True, barmode= 'group'))

    st.header('The popular payment methods')
    purchases_distributed = df.groupby('Payment')['Quantity'].sum().sort_values(ascending= False).reset_index()
    st.plotly_chart(px.pie(data_frame= purchases_distributed, names= 'Payment', values= 'Quantity', hole= 0.5))

    st.header('the average customer rating for each branch')
    avrage_rating_per_branch = df.groupby(['Branch'])['Rating'].mean().sort_values(ascending= False).reset_index()
    st.plotly_chart(px.bar(data_frame= avrage_rating_per_branch, x= 'Branch', y= 'Rating', color= 'Branch', barmode= 'group', text_auto= '0.5'))

    st.header('total sales for each the months')
    sales_per_month = df.groupby('month')['Total'].sum().sort_values(ascending= False).reset_index()
    st.plotly_chart(px.bar(data_frame= sales_per_month, x= 'month', y= 'Total', text_auto= '0.5', labels={'Total' : 'total sales'}))

    st.header(' the top day from each month achives higher sales')
    sales_per_month_day = df.groupby(['month', 'day'])['Total'].sum().sort_values(ascending= False).reset_index()
    st.plotly_chart(px.bar(data_frame= sales_per_month_day , x= 'month', y= 'Total', color= 'day', text_auto= '0.5', 
        labels={'Total' : 'total sales'}, barmode= 'group' ))

    st.header('graph show Which period of the day (morning/afternoon/evening) sees the highest total sales.')
    sales_per_day_period = df.groupby(['day', 'day_period'])['Total'].sum().sort_values(ascending= False).reset_index()
    st.plotly_chart(px.bar(data_frame= sales_per_day_period , x= 'day', y= 'Total', color= 'day_period', text_auto= '0.5',
        labels={'Total' : 'total sales'}, barmode= 'group' ))

    st.header('the gross income distributed for each product lines')
    st.plotly_chart(px.box(data_frame= df, x= 'Product line', y= 'gross income', color= 'Product line'))

    st.header('the gross income distributed per date')
    line_data = df.groupby(['Date'])['gross income'].sum().reset_index()
    st.plotly_chart(px.line(data_frame= line_data, x= 'Date', y= 'gross income'))

    st.header('the gross income distributed per date')
    the_higest_line_income = df.groupby("Product line")['gross income'].sum().sort_values(ascending= False).reset_index()
    st.plotly_chart(px.bar(data_frame= the_higest_line_income, x= 'Product line', y= 'gross income', text_auto= True,
    labels={'gross income' : 'totoal gross income each proudct line'}))

    st.markdown("""<h1 style="color:orange;text-align:center;"> Thank you for reaching here 😇 </h1>""",
             unsafe_allow_html= True)
