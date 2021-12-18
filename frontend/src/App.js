import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import React, { Component } from "react";


class App extends React.Component {

	state = {
		segments: [],
	}

	componentDidMount() {

		let data;

		axios.get('http://localhost:8000/api/segments-list')
			.then(res => {
				data = res.data;
				this.setState({
					segments: data
				});
			})
			.catch(err => { })
	}

	render() {
		return (
			<div>
				{this.state.segments.map((segment) => (
					// <div key={id}>
					<div class="container">
						<table class="table">

							<thead>
								<tr>
									<th>Name</th>
									<th>Date Created</th>
									<th>Last Updated</th>
									<th>Combines</th>
									<th>Totalable</th>
									<th>Render</th>
									<th>Customer</th>
								</tr>
							</thead>
							<tbody>
								<tr>
									<td>{ segment.name }</td>
									<td>{ segment.created_at }</td>
									<td>{ segment.updated_at }</td>
									<td>{ segment.combines }</td>
									<td>{ segment.totalable }</td>
									<td>{ segment.render }</td>
									<td>{ segment.customer }</td>
								</tr>
							</tbody>
						</table>
					</div>
				)
				)}
			</div>
		);
	}
}

export default App;
