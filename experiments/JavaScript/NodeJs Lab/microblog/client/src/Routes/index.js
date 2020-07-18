import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import Login from '../pages/Login';
import Home from '../pages/Home';
import Singup from '../components/Singup';
import AuthRoute from "./AuthRoute";

export default function Routes() {
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/" exact component={Login}/>
                <Route path="/singup" component={Singup}/>
                <AuthRoute path="/home" component={Home}/>
            </Switch>
        </BrowserRouter>
    );
}