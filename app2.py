import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

# 页面配置
st.set_page_config(
    page_title="Chloe WANG个人校招求职简历",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 全局样式
def global_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&display=swap');
    body { font-family: 'Noto Sans SC', sans-serif; color: #333; }
    .header { font-size: 2.5rem; font-weight: 700; color: #2B6CB0; }
    .subheader { font-size: 1.2rem; color: #6B7280; margin-bottom: 1rem; }
    .section-title { color: #2B6CB0; border-bottom: 2px solid #2B6CB0; padding-bottom: 0.5rem; margin: 2rem 0; }
    .achievement { color: #155E75; font-weight: bold; }
    .skill-item { background-color: #F3F4F6; padding: 0.2rem 0.6rem; border-radius: 12px; margin-right: 0.5rem; margin-bottom: 0.5rem; }
    .contact-info { text-align: right; }
    .footer { border-top: 1px solid #E5E7EB; padding: 1rem; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 主页内容
def home_page():
    global_style()
    col1, col2 = st.columns([3, 1], gap="large")
    
    # 左侧个人信息
    with col1:
        st.markdown("<div class='header'>王冰颖 (Chloe Wang)</div>", unsafe_allow_html=True)
        st.markdown("<div class='subheader'>对外经济贸易大学本科+香港中文大学硕士 | 4市场营销与管理咨询领域实习经历 | 数据驱动型决策者</div>", unsafe_allow_html=True)
        st.markdown("""
        拥有美妆、3C跨行业营销策划、数据运营与咨询4段实习经验，擅长通过消费者洞察与数字化手段驱动业务增长。<br>
        熟练运用 SQL、SPSS 等数据分析工具，在小红书平台运营、品牌全案策划、ESG 咨询领域有突出成果。<br>
        工作上的效率至上J人，生活中的自由探索P人。
        """, unsafe_allow_html=True)
    
    # 右侧联系方式（直接用相对路径显示图片）
    with col2:
        st.image("resumepicture1.jpg", width=150)
        add_vertical_space(1)
        st.markdown("<div class='contact-info'>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>手机：</strong> (+86) 18515590199</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>邮箱：</strong> 18515590199@163.com</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>微信：</strong> wby7196</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    add_vertical_space(2)

# 教育背景页面、实习经历页面、项目经历页面、技能与证书页面、main函数等无需修改

# 多页面导航
def main():
    st.sidebar.markdown("# 王冰颖个人简历", unsafe_allow_html=True)
    page = st.sidebar.radio("导航", ["主页", "教育背景", "实习经历", "项目经历", "技能与证书"])
    
    if page == "主页":
        home_page()
    elif page == "教育背景":
        education_page()
    elif page == "实习经历":
        experience_page()
    elif page == "项目经历":
        project_page()
    else:
        skill_page()
    
    st.markdown("<div class='footer'>Created by ❤️ Chloe WANG  | 2025</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()