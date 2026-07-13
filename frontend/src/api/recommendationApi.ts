import { apiClient } from './client';
import type { ContentRecommendation } from '../features/dashboard/types/dashboard';

export type RecommendationsResponse = {
  recommendations: ContentRecommendation[];
};

export const RecommendationApi = {
  async getRecommendations(): Promise<RecommendationsResponse> {
    const response = await apiClient.get<RecommendationsResponse>('/api/recommendations');
    return response.data;
  },
};
