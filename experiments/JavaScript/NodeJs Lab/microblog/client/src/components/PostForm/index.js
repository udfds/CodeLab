import React, { useState } from 'react';

import { Container } from './styles';


export default function PostForm(props) {
    const [text, setText] = useState('');

    const handlePost = async event => {
        event.preventDefault();
        await props.onCreatePost();
        setText('');
    };

    return (
        <Container>
            <textarea placeholder="Write your message" rows={4} 
                value={text} onChange={e => setText(e.target.value)} />
            <div>
                <button onClick={handlePost}>Enter</button>
            </div>
        </Container>
    );
}