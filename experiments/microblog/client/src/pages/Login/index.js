import React from 'react';

import Layout from '../../components/Layout';
import { Container, Content, Input, Button } from './styles';


export default function Login() {
    return (
        <Layout>
            <Container>
                <Content>
                    <div>
                        <label>Username</label>
                        <Input type="text" />
                    </div>
                    <div>
                        <label>Password</label>
                        <Input type="password" />
                    </div>
                    <div>
                        <a href="/singup">Sing up</a>
                        <Button type="submit">Login</Button>
                    </div>
                </Content>
            </Container>
        </Layout>
    );
}
