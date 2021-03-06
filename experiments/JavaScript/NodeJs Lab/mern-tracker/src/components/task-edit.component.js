import React, { Component } from 'react';
import axios from 'axios';
import DatePicker from 'react-datepicker';
import "react-datepicker/dist/react-datepicker.css";

export default class TaskEdit extends Component {

    constructor(props) {
        super(props);

        this.onChangeUsername = this.onChangeUsername.bind(this);
        this.onChangeDescription = this.onChangeDescription.bind(this);
        this.onChangeDuration = this.onChangeDuration.bind(this);
        this.onChangeDate = this.onChangeDate.bind(this);
        this.onSubmit = this.onSubmit.bind(this);

        this.state = {
            username: '',
            description: '',
            duration: 0,
            date: new Date(),
            users: []
        };
    }

    componentDidMount() {
        axios.get('http://localhost:5000/task/' + this.props.match.params.id)
            .then(response => {
                this.setState({
                    username: response.data.username,
                    description: response.data.description,
                    duration: response.data.duration,
                    date: new Date(response.data.date)
                });
            })
            .catch((error) => {
                console.log(error);
            });

        axios.get('http://localhost:5000/user')
            .then(response => {
                if (response.data.length > 0) {
                    this.setState({
                        users: response.data.map(user => user.username),
                        username: response.data[0].username
                    })
                }
            })
            .catch((error) => {
                console.log(error);
            });
    }

    onChangeUsername(event) {
        this.setState({ username: event.target.value });
    }

    onChangeDescription(event) {
        this.setState({ description: event.target.value });
    }

    onChangeDuration(event) {
        this.setState({ duration: event.target.value });
    }

    onChangeDate(date) {
        this.setState({ date: date });
    }

    onSubmit(event) {
        event.preventDefault();

        const task = {
            username: this.state.username,
            description: this.state.description,
            duration: this.state.duration,
            date: this.state.date
        };

        axios.put('http://localhost:5000/task/' + this.props.match.params.id, task)
            .then(response => console.log(response.data));

        window.location = '/';
    }

    render() {
        return (
            <div>
                <h3>Edit task</h3>
                <form onSubmit={this.onSubmit}>
                    <div className="form-group">
                        <label>Username: </label>
                        <select ref="userInput" required className="form-control" value={this.state.username} onChange={this.onChangeUsername}>
                            {
                                this.state.users.map(function (user) {
                                    return <option key={user} value={user}>{user} </option>;
                                })
                            }
                        </select>
                    </div>
                    <div className="form-group">
                        <label>Description: </label>
                        <input type="text" required className="form-control" value={this.state.description} onChange={this.onChangeDescription} />
                    </div>
                    <div className="form-group">
                        <label>Duration (in minutes): </label>
                        <input type="text" className="form-control" value={this.state.duration} onChange={this.onChangeDuration} />
                    </div>
                    <div className="form-group">
                        <label>Date: </label>
                        <div>
                            <DatePicker selected={this.state.date} onChange={this.onChangeDate} />
                        </div>
                    </div>

                    <div className="form-group">
                        <input type="submit" value="Edit task" className="btn btn-primary" />
                    </div>
                </form>
            </div>
        );
    }

}