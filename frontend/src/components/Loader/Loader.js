import React from 'react';  
import './Loader.css';
import { DarkLoader } from '../Functions';


export default class Loader extends React.Component { 

  static messages = [
    'Crunching the data 🗃️',
    'Rebooting the solver',
    'Creating time vortexes 🌀',
    'Analyzing the department 🔎',
    'Taking a break ☕',
    'Implementing math equations 📚',
    'Allocating more memory 💽',
    '‍Meeting teachers\' needs',
    'Trying hard to find the solutions 💡',
    'Extending the breaks',
    'Adding more constraints 🔗',
    'Validating possible solutions 📜',
    'Fetching 192.77.82.68 🌐',
    'Packaging the timetables 📦',
    'Making life simpler 🎉',
    'Debugging 🐞',
    'Burning infeasible timetables 💥'
  ];

  constructor() {
    super();

    this.state = {
      message: 'Crunching the data 🗃️'
    };
  }

  changeMessage() {

    const index = Loader.messages.indexOf(this.state.message);

    this.setState({
      message: index === Loader.messages.length - 1 ? Loader.messages[0] : Loader.messages[index+1]
    });
  }

  componentDidMount() {
    DarkLoader()
    setInterval(this.changeMessage.bind(this), 3000);
  }

  componentWillUnmount() {
    
    clearInterval(this.changeMessage);
  }


  render() {
    return (
      <div className="loader">
        <div className="lds-ellipsis">
          {
            Array.from({ length: 4 }).map((item, i) => <div key={i} />)
          }
        </div>
        <div className="message" id='loader'>
          {this.state.message}
        </div>
      </div>
    );
  }
}