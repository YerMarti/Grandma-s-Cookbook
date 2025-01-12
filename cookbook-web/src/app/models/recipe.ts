export interface Recipe {
    id: number;
    name: string;
    category: string;
    area: string;
    instructions: string;
    thumbnail: string;
    ingredients: { [key: string]: string };
}