import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';

import { Container, Content, Input, Button } from "./styles";
import Layout from '../Layout';
import { ErrorWarning } from '../../pages/Login/styles';

export default function Singup() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const history = useHistory();

    const handleCreate = async event => {
        event.preventDefault();

        if (!!username && !!password) {
            try {
                await axios.post(`${process.env.REACT_APP_SERVER_URL}/users`, { username, password });

                return history.push('/');

            } catch (error) {
                console.error(error);
                setError('Username already in use.');
                setUsername('');
                setPassword('');
            }
        }
    }

    return (
        <Layout>
            <Container>
                <Content>
                    { error && <ErrorWarning>{error}</ErrorWarning> }
                    <div>
                        <label>Username</label>
                        <Input type="text" value={username} onChange={e => setUsername(e.target.value)} />
                    </div>
                    <div>
                        <label>Password</label>
                        <Input type="password" value={password} onChange={e => setPassword(e.target.value)} />
                    </div>
                    <div>
                        <a href="/">Cancel</a>
                        <Button type="submit" onClick={handleCreate} >Create</Button>
                    </div>
                </Content>
            </Container>
        </Layout>
    );
}