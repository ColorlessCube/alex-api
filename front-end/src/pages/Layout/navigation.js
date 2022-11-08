import {Menu} from 'antd';
import {useState} from "react";
import {useNavigate, useLocation} from 'react-router-dom';

function Navigator() {
    const navigate = useNavigate();
    const location = useLocation();
    const [current, setCurrent] = useState(location.pathname);

    const items = [
        {label: '文本格式化', key: '/text/format'}, // 菜单项务必填写 key
        {label: 'blog', key: '/text/blog'},
    ];

    const forwardPage = (key) => {
        setCurrent(key)
        navigate(key)
    }

    return (
        <Menu mode="horizontal"
              items={items}
              defaultSelectedKeys={[current]}
              onClick={(e) => forwardPage(e.key)}
        >
        </Menu>
    )
}

export default Navigator;