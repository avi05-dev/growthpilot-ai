import { apiClient } from './client';
import type { Trend } from '../features/dashboard/types/dashboard';

export type TrendsResponse = {
  trends: Trend[];
};

export const TrendApi = {
  async getTrends(): Promise<TrendsResponse> {
    const response = await apiClient.get<TrendsResponse>('/api/trends');
    return response.data;
  },
};
