import React, { Component } from 'react';
import ScheduleItem from './ScheduleItem';

export default class Schedule extends Component {
  constructor(props) {
    super(props)
  }
  render() {
    return <div>
      {this.props.acetateSchedule.length > 0 ? console.log(this.props.acetateSchedule) : null}
      {this.props.acetateSchedule.map((acetate, index) => {
        {console.log("hello")}
        return <ScheduleItem key={acetate + index} acetate={acetate} count={this.props.countSchedule[index]}/>
      })}
    </div>;
  }
}
