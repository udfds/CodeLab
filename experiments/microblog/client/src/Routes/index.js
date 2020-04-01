import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import Login from '../pages/Login';
import Singup from '../components/Singup';

export default function Routes() {
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/" exact component={Login}/>
                <Route path="/singup" component={Singup}/>
            </Switch>
        </BrowserRouter>
    );
}