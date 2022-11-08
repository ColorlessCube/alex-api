import {useStore} from '../store'
import {useState} from "react";
import TextArea from "antd/es/input/TextArea";
import {observer} from "mobx-react-lite";

function Text() {
    const {textStore} = useStore()
    const [input, setInput] = useState()

    const textHandler = (e) => {
        if (e.keyCode === 13) {
            textStore.textFormat(input)
        }
    }

    return (
        <div>
            <span>输入：</span>
            <TextArea
                rows={6}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyUp={textHandler}
            />
            <br/>
            <br/>
            <span>结果：</span>
            <TextArea
                rows={6}
                value={textStore.text}
            />
        </div>
    )
}

export default observer(Text);