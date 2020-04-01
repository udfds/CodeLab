import React from 'react';

import { Container, Content, Input, Button } from "./styles";
import Layout from '../Layout';

export default function Singup() {
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
                        <a href="/">Cancel</a>
                        <Button type="submit">Create</Button>
                    </div>
                </Content>
            </Container>
        </Layout>
    );
}