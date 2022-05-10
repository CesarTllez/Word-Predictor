import { Component } from '@angular/core';
import { ApiService } from './_service/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Frontend';
  word: string = "";
  placeholder: string = `${this.word} speak`;
  
  constructor(
    private _api: ApiService
  ){}

  write(){
    this._api.getSuggestion(this.word).subscribe(
      response => {
        console.log(response)
      },
      error => {
        console.log(error)
      }
    );
  }
}
