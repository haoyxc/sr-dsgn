import React, { Component } from 'react'

export default class ScheduleItem extends Component {
    constructor(props) {
        super(props)
    }
  render() {
    return (
      <div>
          {this.props.acetate}: {this.props.count}
      </div>
    )
  }
}
