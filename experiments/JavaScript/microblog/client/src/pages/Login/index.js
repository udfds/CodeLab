import React, { useState } from 'react';
import axios from 'axios';
import jwt from 'jsonwebtoken';
import { useHistory } from 'react-router-dom';

import Layout from '../../components/Layout';
import { Container, Content, Input, Button } from './styles';

export default function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const history = useHistory();

    const handleLogin = async event => {
        event.preventDefault();

        if (!!username && !!password) {
            try {
                const response = await axios.post(`${process.env.REACT_APP_SERVER_URL}/login`, { username, password });
                localStorage.setItem('SESSION_TOKEN', response.data);

                return history.push('/home');

            } catch (error) {
                console.error(error);
                if (error.response.status === 404) {
                    setError('Username not found.');
                    setUsername('');
                    setPassword('');

                } else if (error.response.status === 400) {
                    setError('Password wrong.');
                    setPassword('');
                }

            }
        }
    };

    return (
        <Layout>
            <Container>
                <Content>
                    <div>
                        <label>Username</label>
                        <Input type="text" value={username} onChange={e => setUsername(e.target.value)} />
                    </div>
                    <div>
                        <label>Password</label>
                        <Input type="password" value={password} onChange={e => setPassword(e.target.value)} />
                    </div>
                    <div>
                        <a href="/singup">Sing up</a>
                        <Button type="submit" onClick={handleLogin} >Login</Button>
                    </div>
                </Content>
            </Container>
        </Layout>
    );
}
