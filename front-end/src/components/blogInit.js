import uuid from 'react-uuid'
import {useEffect, useState} from "react";
import TextArea from "antd/es/input/TextArea";

function BlogInit() {
    const [init, setInit] = useState()

    useEffect(() => {
        const info = "# title\n" +
        "\n" +
        "> 标识符："+ uuid()+"\n" +
        ">\n" +
        "> 是否公开：是\n" +
        ">\n" +
        "> 分类：技术架构，后端技术\n" +
        ">\n" +
        "> 标签：linux，python"
        setInit(info)
    }, [])

    return (
        <div>
            <TextArea
                rows={10}
                value={init}
            />
        </div>
    )
}

export default BlogInit;