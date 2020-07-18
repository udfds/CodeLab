import React, { Component } from 'react';
import { Link } from 'react-router-dom';

export default class Navbar extends Component {

    render() {
        return (
            <nav className="navbar navbar-dark bg-dark navbar-expand-lg">
                <Link to="/" className="navbar-brand">Task Manager</Link>
                <div className="collapse navbar-collapse">
                    <ul className="navbar-nav mr-auto">
                        <li className="navbar-item">
                            <Link to="/task/list" className="nav-link">Task list</Link>
                        </li>
                        <li className="navbar-item">
                            <Link to="/task/create" className="nav-link">Task create</Link>
                        </li>
                        <li className="navbar-item">
                            <Link to="/user/create" className="nav-link">User create</Link>
                        </li>
                    </ul>
                </div>
            </nav>
        );
    }

}