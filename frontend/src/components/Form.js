import axios from 'axios';
import React, { Component, useState } from 'react';

export default class Form extends Component {
    state = {
        tankInitial: 0,
        tankCapacity: 0,
        downtime: 0,
        butylDemand: 0,
        butylCapacity: 0,
        butylDensity: 0,
        butylProd: 0,
        ethylDemand: 0, 
        ethylCapcity: 0,
        ethylDensity: 0,
        ethylProd: 0
    }
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    async handleSubmit(event) {
        event.preventDefault()
        alert("submitted")
        console.log(this.state)
        const response = await axios.post('http://localhost:5000/flask/submitForm', this.state, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        console.log(response)
        
    }

    handleChange = (evt) => {
        const name = evt.target.name;
        const value = evt.target.value;
        this.setState({[name]: value})
    }

    render() {
        return (
        <form className='input-form container' onSubmit={this.handleSubmit}>
            <div className='input-container'>
                {/* ============================================================= */}
                {/* COLUMN 1 */}
                {/* ============================================================= */}
                <div className='column'>
                    {/* TANK INITIAL CAPACITY */}
                    <div className="form-group col-md-8 col-md-offset-2">
                        <label className='form-label'> Tank Initial Capacity (gallons)</label>
                        <br/>
                        <input name="tankInitial" type="number" onChange={this.handleChange} className="form-input"placeholder='e.g. 100' min='0'></input>
                    </div>
                    {/* TANK CAPACITY */}
                    <div className="form-group col-md-8 col-md-offset-2">
                        <label className='form-label'> Tank Capacity (gallons)</label>
                        <br/>
                        <input name="tankCapacity" type="number" onChange={this.handleChange} className="form-input"placeholder='e.g. 100' min='0'></input>
                    </div>

                    {/* Downtime */}
                    <div>
                        <label className='form-label'> Downtime (Days)</label>
                        <br/>
                        <input name="downtime" type="number" onChange={this.handleChange} classname="form-input" placeholder='e.g. 2'></input> 
                    </div>
                </div>
                {/* ============================================================= */}
                {/* COLUMN 2 */}
                {/* ============================================================= */}
                <div className='column'>
                    <h3 className='form-header'>Butyl Acetate</h3>
                    {/* BUTYL DEMAND */}
                    <div className="form-group col-md-8 col-md-offset-2">
                        <label className='form-label'> Expected Demand (pounds per month)</label>
                        <br/>
                        <input name="butylDemand" type="number" onChange={this.handleChange} className="form-input"placeholder='e.g. 100' min='0'></input>
                    </div>
                    {/* BUTYL CAPACITY */}
                    <div>
                        <label className='form-label'>Production Capacity (pounds per month)</label>
                        <br/>
                        <input name="butylCapacity" type="number" onChange={this.handleChange} classname="form-input" placeholder='e.g. 100'></input> 
                    </div>
                    {/* BUTYL Density */}
                    <div>
                        <label className='form-label'>Density(pounds per gallon)</label>
                        <br/>
                        <input name="butylDensity" type="number" onChange={this.handleChange} classname="form-input" placeholder='e.g. 100'></input> 
                    </div>
                    {/* BUTYL Production rate */}
                    <div>
                        <label className='form-label'>Production rate(pounds per day)</label>
                        <br/>
                        <input name="butylProd" type="number" onChange={this.handleChange} classname="form-input" placeholder='e.g. 100'></input> 
                    </div>
                </div>

                {/* ============================================================= */}
                {/* COLUMN 3 */}
                {/* ============================================================= */}
                <div className='column'>
                    <h3 className='form-header'>Ethyl Acetate</h3>
                    {/* ETHYL DEMAND */}
                    <div className="form-group col-md-8 col-md-offset-2">
                        <label className='form-label'> Expected Demand (pounds per month)</label>
                        <br/>
                        <input name="ethylDemand" type="number" onChange={this.handleChange} className="form-input"placeholder='e.g. 100' min='0'></input>
                    </div>
                    {/* ETHYL CAPACITY */}
                     <div>
                        <label className='form-label'> Production Capacity (pounds per month)</label>
                        <br/>
                        <input name="ethylCapacity" type="number" onChange={this.handleChange} classname="form-input" placeholder='e.g. 100'></input> 
                    </div>
                    {/* ETHYL Density */}
                    <div>
                        <label className='form-label'> Density(pounds per gallon)</label>
                        <br/>
                        <input name="ethylDensity" type="number" onChange={this.handleChange} classname="form-input" placeholder='e.g. 100'></input> 
                    </div>
                    {/* ETHYL Production rate */}
                    <div>
                        <label className='form-label'>Production rate(pounds per day)</label>
                        <br/>
                        <input name="ethylProd" type="number" onChange={this.handleChange} classname="form-input" placeholder='e.g. 100'></input> 
                    </div>
                </div>
                
            </div>
            <div>
                <button type="submit">Submit</button>
            </div>
          </form>
        )
    }
}
