import {Outlet} from 'react-router-dom'
import Navigator from "./navigation"
import {Layout} from 'antd'
import './index.scss'

const {Header, Footer, Content} = Layout


function PageLayout() {
    return (
        <div>
            <Layout>
                <Header className='header'>
                    <Navigator className='navigator'/>
                </Header>
                <Content className='content'><Outlet/></Content>
                <Footer className='footer'>@alex-api</Footer>
            </Layout>
        </div>
    )
}

export default PageLayout;