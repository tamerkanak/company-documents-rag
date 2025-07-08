import streamlit as st

def render_footer():
    footer = '''
    <style>
    .footer-modern {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: rgba(40, 44, 52, 0.85);
        color: #fff;
        text-align: center;
        padding: 16px 0 10px 0;
        font-size: 17px;
        font-family: 'Segoe UI', 'Roboto', 'Arial', sans-serif;
        z-index: 100;
        box-shadow: 0 -2px 16px rgba(44,62,80,0.10);
        border-top: 1px solid rgba(80,80,80,0.18);
        letter-spacing: 0.01em;
        backdrop-filter: blur(6px);
    }
    .footer-modern-content {
        max-width: 980px;
        margin: 0 auto;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 18px;
    }
    .footer-modern a {
        color: #ffd700;
        text-decoration: none;
        margin: 0 14px;
        display: inline-flex;
        align-items: center;
        transition: color 0.2s;
    }
    .footer-modern a:hover {
        color: #fff;
    }
    .footer-modern .icon {
        width: 24px;
        height: 24px;
        margin-right: 0;
        vertical-align: middle;
        fill: #ffd700;
        transition: fill 0.2s;
    }
    .footer-modern a:hover .icon {
        fill: #fff;
    }
    @media (max-width: 1100px) {
        .footer-modern-content { max-width: 100vw; padding: 0 16px; }
    }
    @media (max-width: 600px) {
        .footer-modern { font-size: 14px; padding: 10px 0 6px 0; }
        .footer-modern .icon { width: 20px; height: 20px; }
        .footer-modern-content { gap: 10px; }
    }
    </style>
    <div class="footer-modern">
      <div class="footer-modern-content">
        Geliştirici: Tamer Kanak &nbsp;|&nbsp;
        <a href="https://www.linkedin.com/in/tamerkanak" target="_blank">
          <svg class="icon" viewBox="0 0 24 24"><path d="M19 0h-14c-2.76 0-5 2.24-5 5v14c0 2.76 2.24 5 5 5h14c2.76 0 5-2.24 5-5v-14c0-2.76-2.24-5-5-5zm-11 19h-3v-10h3v10zm-1.5-11.28c-.97 0-1.75-.79-1.75-1.75s.78-1.75 1.75-1.75 1.75.79 1.75 1.75-.78 1.75-1.75 1.75zm15.5 11.28h-3v-5.6c0-1.34-.03-3.07-1.87-3.07-1.87 0-2.16 1.46-2.16 2.97v5.7h-3v-10h2.89v1.36h.04c.4-.75 1.38-1.54 2.84-1.54 3.04 0 3.6 2 3.6 4.59v5.59z"/></svg>
        </a>
        &nbsp;|&nbsp;
        <a href="https://github.com/tamerkanak" target="_blank">
          <svg class="icon" viewBox="0 0 24 24"><path d="M12 .5c-6.62 0-12 5.38-12 12 0 5.3 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.756-1.333-1.756-1.09-.745.083-.729.083-.729 1.205.085 1.84 1.237 1.84 1.237 1.07 1.834 2.807 1.304 3.492.997.108-.775.418-1.305.762-1.605-2.665-.305-5.466-1.332-5.466-5.93 0-1.31.468-2.38 1.236-3.22-.124-.304-.535-1.527.117-3.176 0 0 1.008-.322 3.3 1.23.96-.267 1.98-.399 3-.404 1.02.005 2.04.137 3 .404 2.29-1.552 3.297-1.23 3.297-1.23.653 1.649.242 2.872.12 3.176.77.84 1.235 1.91 1.235 3.22 0 4.61-2.803 5.624-5.475 5.921.43.372.823 1.102.823 2.222 0 1.606-.015 2.898-.015 3.293 0 .322.218.694.825.576 4.765-1.587 8.2-6.086 8.2-11.384 0-6.62-5.38-12-12-12z"/></svg>
        </a>
      </div>
    </div>
    '''
    st.markdown(footer, unsafe_allow_html=True) 