import React from 'react';
import { BrowserRouter as Router, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

import Navbar from "./components/navbar.component";
import TaskList from "./components/task-list.component";
import TaskEdit from "./components/task-edit.component";
import TaskCreate from "./components/task-create.component";
import UserCreate from "./components/user-create.component";

function App() {
  return (
    <Router>
      <div className="container">
        <Navbar />
        <br />
        <Route path="/" exact component={TaskList} />
        <Route path="/task/list" component={TaskList} />
        <Route path="/task/edit/:id" component={TaskEdit} />
        <Route path="/task/create" component={TaskCreate} />
        <Route path="/user/create" component={UserCreate} />
      </div>
    </Router>
  );
}

export default App;
