import React from 'react';  
import './Loader.css';
import { DarkLoader } from '../Functions';


export default class Loader extends React.Component { 

  static messages = [
    '🚀Going to get the Content 🚀',
'🗃️ Crunching the Content 🗃️',
'🧝 Hiring some Elves for Work 🧝',
'💥 Burning extra Stuff 💥',
'📷 Taking pictures of Important Parts 📷',
'🗒️ Summarizing the Content 🗒️',
'💤 Falling Asleep 💤',
'♻️ Recycling leftover Papers ♻️',
'🔗 Fetching useful Links 🔗',
'🌀 Creating Time Vortexes 🌀',
'☕ Taking a break ☕',
'📜 Generating the Notes 📜',
'📦 Packaging the Notes 📦',
'💵 Paying the Elves 💵',
'🎉 Making Life Simpler 🎉',
'🧠 Searching my brain for data 🧠',
'👨‍💻 Validating the Notes 👨‍💻'
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