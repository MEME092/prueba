export type CategorySlug = 'tramites' | 'python-flet' | 'apps-moviles' | 'herramientas';

export interface FAQItem {
  question: string;
  answer: string;
}

export interface QuickStep {
  id: string;
  title: string;
  description: string;
  commandOrAction?: string;
}

export interface Category {
  slug: CategorySlug;
  name: string;
  description: string;
  color?: string;
}

export interface Article {
  id: number;
  title: string;
  slug: string;
  excerpt: string;
  content: string;
  category_slug: CategorySlug;
  author: string;
  featured_image: string;
  image_caption?: string;
  device_tested?: string;
  copyright_notice?: string;
  created_at: string;
  status: 'Publicado' | 'Borrador';
  read_time_minutes?: number;
  difficulty?: 'Principiante' | 'Intermedio' | 'Avanzado';
  estimated_time?: string;
  quick_steps?: QuickStep[];
  faqs?: FAQItem[];
  tested_notes?: string;
}

export interface Author {
  name: string;
  role: string;
  university: string;
  location: string;
  bio: string;
  avatar_url?: string;
  github?: string;
  linkedin?: string;
  email: string;
}

export type AuthorProfile = Author;
