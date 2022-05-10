import { Component } from '@angular/core';
import { ApiService } from './_service/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Frontend';
  word: string;
  suggestionWord: any;
  
  constructor(
    private _api: ApiService
  ){
    this.word = "";
    this.suggestionWord = {
      "suggestion": "",
      "word": ""
    }
  }

  write(){
    this._api.getSuggestion(this.word).subscribe(
      response => {
        this.suggestionWord = response;
        console.log(response)
      },
      error => {
        console.log(error)
      }
    );
  }
}
