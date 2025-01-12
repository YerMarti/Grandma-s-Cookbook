import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Recipe } from '../models/recipe';

@Injectable({
  providedIn: 'root'
})
export class RecipeService {

  private apiUrl:string = 'http://localhost:50002/recipes';

  constructor(private http:HttpClient) { }

  public searchRecipes(searchText:string): Observable<any[]> {
    const params = new HttpParams().set('name', searchText);

    return this.http.get<any[]>(`${this.apiUrl}/search`, { params: params });
  }

  public randomRecipe(): Observable<any> {
    const headers = new HttpHeaders({'Content-Type': 'application/json'});

    return this.http.get<any>(`${this.apiUrl}/random`, {headers});
  }

  public getRecipe(recipeId:string): Observable<any> {
    const headers = new HttpHeaders({'Content-Type': 'application/json'});

    return this.http.get<any>(`${this.apiUrl}/${recipeId}`, {headers});
  }
  
}
