import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable, WritableSignal, signal } from '@angular/core';
import { Observable } from 'rxjs';
import { User } from '../models/user';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private loggedUsername: WritableSignal<string> = signal<string>("");
  private apiUrl:string = 'http://localhost:50002/users';

  constructor(private http:HttpClient) { }

  public login(usernameText:string, passwordText:string): Observable<any> {
    console.log("login");
    const data = {username: usernameText, password: passwordText};
    console.log(data);
    const headers = new HttpHeaders({'Content-Type': 'application/json'});
    
    return this.http.post<any>(`${this.apiUrl}/login`, data, {headers});
  }

  public register(usernameText:string, passwordText:string): Observable<any> {
    console.log("register");
    const data = {username: usernameText, password: passwordText};
    console.log(data);
    const headers = new HttpHeaders({'Content-Type': 'application/json'});
  
    return this.http.post<any>(`${this.apiUrl}/register`, data, {headers});
  }

  public addFavoriteRecipe(recipeId:string): Observable<any> {
    console.log("addFavoriteRecipe");
    const data = {username: this.loggedUsername, recipeId: recipeId};
    console.log(data);
    const headers = new HttpHeaders({'Content-Type': 'application/json'});
    
    return this.http.post<any>(`${this.apiUrl}/${this.loggedUsername}/favorite`, data, {headers});
  }

  public getFavoriteRecipes(username:string): Observable<any> {
    console.log("getFavoriteRecipes");
    console.log(username);
    return this.http.get<any>(`${this.apiUrl}/${username}/favorites`);
  }

  public getLoggedUsername(): string {
    console.log("getLoggedUsername");
    console.log(this.loggedUsername());
    return this.loggedUsername();
  }

  public setLoggedUsername(username:string): void {
    console.log("setLoggedUsername");
    this.loggedUsername.set(username);
  }

}
