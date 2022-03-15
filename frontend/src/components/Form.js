import axios from 'axios';
import React, { Component, useState } from 'react';
import Schedule from './Schedule';

export default class Form extends Component {
    state = {
        tankInitial: 0,
        tankCapacity: 0,
        turnover: 0,
        butylDemand: 0,
        butylCapacity: 0,
        butylDensity: 1, // avoid divide by 0
        butylProd: 0,
        ethylDemand: 0, 
        ethylCapacity: 0,
        ethylDensity: 1, // avoid divide by 0
        ethylProd: 0,
        scheduleAcetateList: [],
        scheduleCountList: []
    }
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this)
        this.parseSched = this.parseSched.bind(this)
    }

    getAcetateFromInt(acetateInt) {
        if (acetateInt === -1) {
            return "Turnover"
        } else if (acetateInt === 0) {
            return "Downtime"
        } else if (acetateInt === 1) {
            return "Butyl"
        } else {
            return "Ethyl"
        }
    }

    parseSched(schedule) {
        let lastAcetate = schedule[0]
        console.log("LAST ACETATE: ", lastAcetate)
        let count = 1
        let acetateList = []
        let countList = []
        for (let i = 1; i < schedule.length; i++) {
            const acetateInt = schedule[i]
            if (acetateInt === lastAcetate) {
                count++
            } else {
                let acetate = this.getAcetateFromInt(lastAcetate)
                acetateList.push(acetate)
                countList.push(count)
                lastAcetate = acetateInt
                count = 1
            }
        }
        acetateList.push(this.getAcetateFromInt(lastAcetate))
        countList.push(count)
        console.log("FINAL ACETATE: ", acetateList)
        console.log("FINAL COUNT: ", countList)
        this.setState({scheduleAcetateList: acetateList, scheduleCountList: countList})
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
        let schedule = response.data.schedule
        console.log(schedule)
        this.parseSched(schedule)
    }

    handleChange = (evt) => {
        const name = evt.target.name;
        const value = evt.target.value;
        this.setState({[name]: value})
    }

    render() {
        return (
        <div>
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
                            <input name="tankInitial" type="number" step="0.01" onChange={this.handleChange} className="form-input"placeholder='e.g. 0' min='0'></input>
                        </div>
                        {/* TANK CAPACITY */}
                        <div className="form-group col-md-8 col-md-offset-2">
                            <label className='form-label'> Tank Capacity (gallons)</label>
                            <br/>
                            <input name="tankCapacity" type="number" step="0.01" onChange={this.handleChange} className="form-input"placeholder='e.g. 1000000000' min='0'></input>
                        </div>

                        {/* Turnover */}
                        <div>
                            <label className='form-label'> Turnover (Days)</label>
                            <br/>
                            <input name="turnover" type="number" step="0.01" onChange={this.handleChange} classname="form-input" placeholder='e.g. 2'></input> 
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
                            <input name="butylDemand" type="number" step="0.01" onChange={this.handleChange} className="form-input"placeholder='e.g. 52000' min='0'></input>
                        </div>
                        {/* BUTYL CAPACITY */}
                        <div>
                            <label className='form-label'>Production Capacity (pounds per month)</label>
                            <br/>
                            <input name="butylCapacity" type="number" step="0.01" onChange={this.handleChange} classname="form-input" placeholder='e.g. 104000'></input> 
                        </div>
                        {/* BUTYL Density */}
                        <div>
                            <label className='form-label'>Density(pounds per gallon)</label>
                            <br/>
                            <input name="butylDensity" type="number" step="0.01" onChange={this.handleChange} classname="form-input" placeholder='e.g. 7.4'></input> 
                        </div>
                        {/* BUTYL Production rate */}
                        <div>
                            <label className='form-label'>Production rate(pounds per day)</label>
                            <br/>
                            <input name="butylProd" type="number" step="0.01" onChange={this.handleChange} classname="form-input" placeholder='e.g. 3500'></input> 
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
                            <input name="ethylDemand" type="number" step="0.01" onChange={this.handleChange} className="form-input"placeholder='e.g. 52000' min='0'></input>
                        </div>
                        {/* ETHYL CAPACITY */}
                        <div>
                            <label className='form-label'> Production Capacity (pounds per month)</label>
                            <br/>
                            <input name="ethylCapacity" type="number" step="0.01" onChange={this.handleChange} classname="form-input" placeholder='e.g. 104000'></input> 
                        </div>
                        {/* ETHYL Density */}
                        <div>
                            <label className='form-label'> Density(pounds per gallon)</label>
                            <br/>
                            <input name="ethylDensity" type="number" step="0.01" onChange={this.handleChange} classname="form-input" placeholder='e.g. 7.5'></input> 
                        </div>
                        {/* ETHYL Production rate */}
                        <div>
                            <label className='form-label'>Production rate(pounds per day)</label>
                            <br/>
                            <input name="ethylProd" type="number" step="0.01" onChange={this.handleChange} classname="form-input" placeholder='e.g. 3500'></input> 
                        </div>
                    </div>
                    
                </div>
                <div>
                    <button type="submit">Submit</button>
                </div>
            </form>
            {/* FOR THE RESPONSE */}
            <Schedule acetateSchedule={this.state.scheduleAcetateList} countSchedule={this.state.scheduleCountList}></Schedule>
          </div>
        )
    }
}
