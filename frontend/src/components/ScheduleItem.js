import React, { Component } from 'react'

export default class ScheduleItem extends Component {
    constructor(props) {
        super(props)
    }
  render() {
    return (
      <div>
         <p className='sched-item'> {this.props.acetate}: {this.props.count} days </p>
      </div>
    )
  }
}
